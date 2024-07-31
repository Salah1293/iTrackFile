from django.forms import ValidationError

from iTrackFiles.settings import BASE_DIR
from .models import *
from batches.models import *
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponseBadRequest, JsonResponse
from django.core.files.base import ContentFile
# from pytwain import Twain
from io import BytesIO
from datetime import datetime, timezone
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db import IntegrityError, transaction
from django.core.files.storage import default_storage
from PIL import Image



def get_job_data(job_id):
        
    fields = PvcapIndex1.objects.filter(jobid=job_id).values_list('fieldname', flat=True)
    index_ids = PvcapIndex1.objects.filter(jobid=job_id).values_list('indexid', flat=True)    

    fields = [field for field in fields if field != 'Date']
    return fields, index_ids, job_id



def save_form_data(job_id, form_data, status, batch_id):
    
    fields_with_index_ids = PvcapIndex1.objects.filter(jobid=job_id).values_list('indexid', 'fieldname')
    index_id_map = {fieldname: indexid for indexid, fieldname in fields_with_index_ids}

    for fieldname, value in form_data.items():
        if fieldname in index_id_map:
            index_id = index_id_map[fieldname]
            
            PvcapIndexvalue1.objects.create(
                jobid=job_id,
                indexid=index_id,
                value=value,
                batchid=batch_id,
                documentid=0,
                detailsetid=None,
                confidence=None,
                rowindex=None
            )

    saved_values = PvcapIndexvalue1.objects.filter(jobid=job_id, batchid=batch_id)
    for saved_value in saved_values:
        print(saved_value)

    
    
    batch = PvcapBatch1.objects.get(batchid=batch_id)
    
    if status == 'complete':
        batch.iscomplete = True
    elif status == 'incomplete':
        batch.iscomplete = False
    batch.save()




def map_fields_to_columns(job_id):
    section_name = PvcapJob1.objects.get(jobid=job_id).name
    field_to_column_mapping = {
        'HR': {'Last Name': 'docindex1', 'First Name': 'docindex2', 'EIN': 'docindex3', 'Employment Type': 'docindex4', 'Document Type': 'docindex6'},
        'Historic Order Books': {'Book Type': 'docindex1', 'Year': 'docindex2', 'Page A': 'docindex3', 'Page B': 'docindex4'},
        'Historic Index Cards': {'Last Name': 'docindex1', 'First Name': 'docindex2', 'Subject': 'docindex3', 'Record Source': 'docindex4', 'Book Record': 'docindex5', 'Page': 'docindex6', 'Date': 'docindex7', 'Comments': 'docindex8', 'Instrument': 'docindex9', 'Status': 'docindex10', 'Owner': 'docindex11', 'Dates before 1753': 'docindex12'}
    }
    return field_to_column_mapping.get(section_name, {})



def count_export_folders(base_path):
    folders = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
    export_folders = [f for f in folders if f.startswith('Export')]
    return len(export_folders)



def create_path(section_name):
    if section_name == 'HR':
        # base_path = '\\s80iTrackPPR01\\PVDocs\\Monitored Import Path\\HR\\'
        base_path = 'E:\\Projects\\iTrackFiles collection\\images'
    elif section_name == 'Historic Order Books':
        # base_path = '\\s80iTrackPPR01\\PVDocs\\Monitored Import Path\\Historic Order Books\\'
        base_path = 'E:\\Projects\\iTrackFiles collection\\images'
    elif section_name == 'Historic Index Cards':
        # base_path = '\\s80iTrackPPR01\\PVDocs\\Monitored Import Path\\Historic Index Cards\\'
        base_path = 'E:\Projects\iTrackFiles collection\images'
    else:
        print("Invalid section name:", section_name)
        return
    

    export_count = count_export_folders(base_path)
    new_folder = f'Export{export_count + 1}'
    full_path = os.path.join(base_path, new_folder)

    os.makedirs(full_path, exist_ok=True)

    full_path = os.path.join(full_path, 'DATAGRP\\')
    os.makedirs(full_path, exist_ok=True)


    start_num = PvdmDg1.objects.count() + 1
    
    dg_entry = PvdmDg1.objects.create(
        dgname=start_num,
        path=full_path, 
        type=1,  
        lastupdatetime=datetime.now(),
        size=0,
        readwrite=True,  
        origdgname=0,
        dginfo=0,
    )

    return dg_entry.dgid

def save_field_data(form_data, job_id, dg_id):
    section_name = PvcapJob1.objects.filter(jobid=job_id).values_list('name', flat=True).first()

    if section_name == 'HR':
        table_model = PvdmDocs15
    elif section_name == 'Historic Order Books':
        table_model = PvdmDocs113
    elif section_name == 'Historic Index Cards':
        table_model = PvdmDocs114
    else:
        return None

    column_mapping = map_fields_to_columns(job_id)

    instance = table_model()
    instance.jobid = job_id

    if section_name in ['HR', 'Historic Order Books', 'Historic Index Cards']:
        instance.createdate = datetime.now()
        instance.dupeid = 0
        instance.dgid = dg_id
        instance.ftindex = 0
        instance.sourcedocid = 0

    for fieldname, value in form_data.items():
        column_name = column_mapping.get(fieldname)
        if column_name:
            if 'date' in column_name.lower():
                if not value:  
                    continue
                try:
                    value = datetime.strptime(value, '%Y-%m-%d')  
                except ValueError as ve:
                    continue
            setattr(instance, column_name.lower(), value)

    try:
        instance.save()
        return instance.docid
    


    except ValidationError as ve:
        return None
  


def save_image_names_to_database(docid, uploaded_images, section_name, image_count, batch_id, dg_id):

    if section_name == 'HR':
        table_model = PvdmObjs15
    elif section_name == 'Historic Order Books':
        table_model = PvdmObjs113
    elif section_name == 'Historic Index Cards':
        table_model = PvdmObjs114
    else:
        print("Invalid section name:", section_name)
        return


    dg_path = PvdmDg1.objects.get(dgid=dg_id).path

    base_path = os.path.join(dg_path, 'Images', '0', '0', '0')

    if not os.path.exists(base_path):
        os.makedirs(base_path, exist_ok=True)


    saved_image_paths = []

    for image_content in uploaded_images:


        image_path = os.path.join(settings.MEDIA_ROOT, image_content.lstrip('/'))
        print('#####image path:', image_path)


        image_name = os.path.basename(image_path)
        print('@@@@@@image name:', image_name)
        save_path = os.path.join(base_path, image_name)

        if not os.path.exists(image_path):
            print(f"Image file does not exist: {image_content}")
            continue

        try:
            with Image.open(image_path) as img:
                img.save(save_path)
                saved_image_paths.append(image_name)
        except Exception as e:
            print(f"error saving image {image_content} locally: {e}")


    filelist = ''.join([f"Images/0/0/0/{image_name}" for  image_name in saved_image_paths])
    
 
    table_model.objects.create(
        docid=docid,
        objtype=1,
        hashtype=1,
        hashinfo='',
        filelist=filelist,
        pages=image_count,
        versionnum=1,
        versiontime=datetime.now(),
        versioncreator='system',
        versioncomments='',
        dgid=dg_id,
        trashuserid=0,
        trashdatetime=None,
        totalbytes=0
    )
