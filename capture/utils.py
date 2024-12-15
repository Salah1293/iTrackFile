import base64
import io
import re
import shutil
from django.forms import ValidationError, model_to_dict
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
from urllib.parse import unquote


########################### CREATE BATCHES ###################################
# RETRIVE FILDS NAME FROM CAPTURE FORM TABLE ALLED INDEX1
def get_job_data(job_id):
    fields = PvcapIndex1.objects.filter(
        jobid=job_id).values_list('fieldname', flat=True)
    index_ids = PvcapIndex1.objects.filter(
        jobid=job_id).values_list('indexid', flat=True)
    return fields, index_ids, job_id

# SAVE VALUE USER ENTRED IN INDEX TABLE
def save_form_data(job_id, form_data, batch_id, status=None):

    fields_with_index_ids = PvcapIndex1.objects.filter(
        jobid=job_id).values_list('indexid', 'fieldname')
    
    index_id_map = {fieldname: indexid for indexid,
                    fieldname in fields_with_index_ids}

    for fieldname, value in form_data.items():
        if fieldname in index_id_map:
            index_id = index_id_map[fieldname]

            PvcapIndexvalue1.objects.create(
                jobid=job_id,
                indexid=index_id,
                value=value,
                batchid=batch_id,
                bundleid=0,
                detailsetid=None,
                confidence=None,
                rowindex=None
            )

    batch = PvcapBatch1.objects.get(batchid=batch_id)

    if status is not None:
        if status == 'complete':
            batch.iscomplete = True
        elif status == 'incomplete':
            batch.iscomplete = False
        batch.save()

# CcOUNT EXPORT FOLDER TO MAKE THE NUMBER INCREMENRED
def count_export_folders(base_path):
    folders = [d for d in os.listdir(
        base_path) if os.path.isdir(os.path.join(base_path, d))]
    export_folders = [f for f in folders if f.startswith('Export')]
    return len(export_folders)

# CREATE PATH
def create_path(section_name):
    if section_name == 'HR':
        base_path = 'E:\\Projects\\Django\\iTrackFiles collections\\images'
    elif section_name == 'Historic Order Books':
        base_path = 'E:\\Projects\\Django\\iTrackFiles collections\\images'
    elif section_name == 'Historic Index Cards':
       base_path = 'E:\\Projects\\Django\\iTrackFiles collections\\images'
    else:
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

# EVERY COLUMN REALTED TO FIELD LABEL
def map_fields_to_columns(job_id):
    section_name = PvcapJob1.objects.get(jobid=job_id).name
    field_to_column_mapping = {
        'HR': {'Last Name': 'docindex1', 'First Name': 'docindex2', 'EIN': 'docindex3', 'Employment Type': 'docindex4', 'Document Type': 'docindex6'},
        'Historic Order Books': {'Book Type': 'docindex1', 'Year': 'docindex2', 'Page A': 'docindex3', 'Page B': 'docindex4'},
        'Historic Index Cards': {'Last Name': 'docindex1', 'First Name': 'docindex2', 'Subject': 'docindex3', 'Record Source': 'docindex4', 'Book Record': 'docindex5', 'Page': 'docindex6', 'Date': 'docindex7', 'Comments': 'docindex8', 'Instrument': 'docindex9', 'Status': 'docindex10', 'Owner': 'docindex11', 'Dates before 1753': 'docindex12'}
    }
    return field_to_column_mapping.get(section_name, {})

# SAVE COMPLE OR INCOMPLES VALUES IN DOCS TABLE
def save_field_data(form_data, job_id, dg_id, batch_id):
    section_name = PvcapJob1.objects.filter(
        jobid=job_id).values_list('name', flat=True).first()

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
        instance.batchid = batch_id

    for fieldname, value in form_data.items():
        column_name = column_mapping.get(fieldname)
        if column_name:
            if 'date' in column_name.lower():
                if not value :
                    continue
                try:
                    value = datetime(value, '%Y-%m-%d')
                except ValueError as ve:
                    print("invalid datetime format")
                    continue
            elif value is None or value == "":
                continue
            setattr(instance, column_name.lower(), value)

    try:
        instance.save()
        return instance.docid

    except ValidationError as e:
        return None


#SAVE IMAGE NAME IN OBJ
def save_image_names_to_database(docid, uploaded_images, section_name, image_count, batch_id, dg_id):

    if section_name == 'HR':
        table_model = PvdmObjs15
    elif section_name == 'Historic Order Books':
        table_model = PvdmObjs113
    elif section_name == 'Historic Index Cards':
        table_model = PvdmObjs114
    else:
        return

    dg_path = PvdmDg1.objects.get(dgid=dg_id).path

    base_path = os.path.join(dg_path, 'Images', '0', '0', '0')

    if not os.path.exists(base_path):
        os.makedirs(base_path, exist_ok=True)

    saved_image_paths = []


    for image_content in uploaded_images:

        image_path = os.path.join(
            settings.MEDIA_ROOT, image_content.lstrip('/'))
        image_path = unquote(image_path)




        image_name = os.path.basename(image_path)
        save_path = os.path.join(base_path, image_name)
        if not os.path.exists(image_path):
            continue

        try:
            with Image.open(image_path) as img:
                img.save(save_path)
                saved_image_paths.append(image_name)
        except Exception as e:
            print(f"error saving image {image_content} locally: {e}")

    filelist = ''.join(
        [f"Images/0/0/0/{image_name}" for image_name in saved_image_paths])
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



# CONVERT TIFF OR ANY EXTENTION TO JPEG
def convert_image_to_jpg(image):
    img = Image.open(image)
    images = []

    while True:
        buffer = io.BytesIO()
        img.convert('RGB').save(buffer, format='JPEG')
        buffer.seek(0)
        images.append(buffer.read())

        try:
            img.seek(img.tell() + 1)
        except EOFError:
            break

    return images

# DELETE BATCH DIR FROM MEDIA AFTER WE CLICKED COMPLETE OR INCOMPLTE
def delete_batch_dir(batch_id):
    media_root = settings.MEDIA_ROOT
    batch_dir = os.path.join(media_root, f'batch_{batch_id}')  

    try:
        if os.path.exists(batch_dir) and os.path.isdir(batch_dir):
            shutil.rmtree(batch_dir) 
        else:
            print(f"Batch directory {batch_dir} does not exist.")
    except Exception as e:
        print(f"Error deleting batch directory {batch_dir}: {e}")


def get_client_ip(request):
   
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



#function to move images to created bundle dir
def save_bundle_images(batchid, bundleid, uploaded_images=None, image_name=None):
    batch_dir = os.path.join(settings.MEDIA_ROOT, f'batch_{batchid}')
    os.makedirs(batch_dir, exist_ok=True)  

    bundle_dir = os.path.join(batch_dir, f'bundle_{bundleid}')
    os.makedirs(bundle_dir, exist_ok=True)

    if uploaded_images:
        for img in uploaded_images:
            img_name = os.path.basename(img)
            original_image_path = os.path.join(settings.MEDIA_ROOT, img.lstrip('/')) 
            batch_image_path = os.path.join(batch_dir, img_name)  

            try:
                if os.path.exists(original_image_path):
                    shutil.move(original_image_path, batch_image_path)
            except Exception as e:
                continue  

    for img in os.listdir(batch_dir):
        img_path = os.path.join(batch_dir, img)
        if os.path.isfile(img_path):  
            bundle_image_path = os.path.join(bundle_dir, img)  

            if image_name:
                if img.lower() == image_name.lower():
                    break

                try:
                    if os.path.exists(img_path):
                        shutil.move(img_path, bundle_image_path)
                except Exception as e:
                    print(f"Exception moving image {img} to bundle dir: {e}")
            else:
                try:
                    if os.path.exists(img_path):
                        shutil.move(img_path, bundle_image_path)
                except Exception as e:
                    print(f"Exception moving image {img} to bundle dir: {e}")




#function to save bundle data to PvcapIndexvalue1 table
def save_bundle_form_data(job_id, form_data, batch_id, bundleid):

    fields_with_index_ids = PvcapIndex1.objects.filter(
        jobid=job_id).values_list('indexid', 'fieldname')
        
    index_id_map = {fieldname: indexid for indexid,
                    fieldname in fields_with_index_ids}
    
    for fieldname, value in form_data.items():
        if fieldname in index_id_map:
            index_id = index_id_map[fieldname]

            PvcapIndexvalue1.objects.create(
                jobid=job_id,
                indexid=index_id,
                value=value,
                batchid=batch_id,
                bundleid=bundleid,
                detailsetid=None,
                confidence=None,
                rowindex=None
            )




#function to create last bundle
def create_last_bundle(batch_id, job_id, form_data):
    try:
        bundle = PvcapBundle.objects.create(
            batchid=batch_id,
            createdate=datetime.now()
        )
    except Exception as e:
        print('exception is:', e)
    images_list = []
    for filename in os.listdir(settings.MEDIA_ROOT):
        file_path = os.path.join(settings.MEDIA_ROOT, filename)
        if os.path.isfile(file_path):
            image_name = os.path.basename(file_path)
            images_list.append(f'/{image_name}')

        
    save_bundle_images(batch_id, bundle.bundleid, images_list)

    save_bundle_form_data(job_id, form_data, batch_id, bundle.bundleid)       


#funtion to save images names to OBJ table
def save_bundle_image_names_to_database(docid, section_name, batch_id, bundle_id, dg_id):

    if section_name == 'HR':
        table_model = PvdmObjs15
    elif section_name == 'Historic Order Books':
        table_model = PvdmObjs113
    elif section_name == 'Historic Index Cards':
        table_model = PvdmObjs114
    else:
        return

    bundle_dir = os.path.join(settings.MEDIA_ROOT, f'batch_{batch_id}', f'bundle_{bundle_id}')

    if not os.path.exists(bundle_dir):
        return

    dg_path = PvdmDg1.objects.get(dgid=dg_id).path
    base_path = os.path.join(dg_path, 'Images', '0', '0', '0')
    if not os.path.exists(base_path):
        os.makedirs(base_path, exist_ok=True)

    saved_image_paths = []
    image_count = 0  

    for image_name in os.listdir(bundle_dir):
        image_path = os.path.join(bundle_dir, image_name)

        if not os.path.exists(image_path) or not image_name.lower().endswith(('.jpg', '.png', '.tif')):
            continue  

        save_path = os.path.join(base_path, image_name)
        try:
            with Image.open(image_path) as img:
                img.save(save_path)
                saved_image_paths.append(image_name)
                image_count += 1  
        except Exception as e:
            print(f"Error saving image {image_name} locally: {e}")

    filelist = ''.join([f"Images/0/0/0/{image_name}" for image_name in saved_image_paths])

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


