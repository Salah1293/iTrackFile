import base64
import io
import re
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

    fields = [field for field in fields if field != 'Date']
    return fields, index_ids, job_id

# SAVE VALUE USER ENTRED IN INDEX TABLE
def save_form_data(job_id, form_data, status, batch_id):

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
                documentid=0,
                detailsetid=None,
                confidence=None,
                rowindex=None
            )

    saved_values = PvcapIndexvalue1.objects.filter(
        jobid=job_id, batchid=batch_id)
   

    batch = PvcapBatch1.objects.get(batchid=batch_id)

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
        base_path = 'E:\\PVDocs\\Monitored Import Path\\HR\\'
        # base_path = 'E:\\Projects\\iTrackFiles collection\\images'
    elif section_name == 'Historic Order Books':
        base_path = 'E:\\PVDocs\\Monitored Import Path\\HistoricOrderBooks\\'
        # base_path = 'E:\\Projects\\iTrackFiles collection\\images'
    elif section_name == 'Historic Index Cards':
        base_path = 'E:\\PVDocs\\Monitored Import Path\\HistoricIndexCards\\'
       # base_path = 'E:\Projects\iTrackFiles collection\images'
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

#SAVE IMAGE NAME IN OBJ
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

# DELETE IMAGES FROM MEDIA AFTER WE CLICKED COMPLETE OR INCOMPLTE
def delete_images(image_urls):
    for image_url in image_urls:
        image_path = os.path.join(settings.MEDIA_ROOT, image_url.lstrip('/'))
        try:
            if os.path.exists(image_path):
                os.remove(image_path)
        except Exception as e:
            print(f"Error deleting image {image_path}: {e}")
            
#################################UPDATE BATCHES(EDIT INCOMPLETE BATCHES######################################################
#RETRIVE OLD DATA FROM INCOMPLTE TO FULLFILLED FOR USER TO COMPLE FROM DOCS TABLE
def fields_conversion(batchid, jobid):

    job_name = PvcapJob1.objects.get(jobid=jobid).name
    field_to_column_mapping = {
        'HR': {'Last Name': 'docindex1', 'First Name': 'docindex2', 'EIN': 'docindex3', 'Employment Type': 'docindex4', 'Document Type': 'docindex6'},
        'Historic Order Books': {'Book Type': 'docindex1', 'Year': 'docindex2', 'Page A': 'docindex3', 'Page B': 'docindex4'},
        'Historic Index Cards': {'Last Name': 'docindex1', 'First Name': 'docindex2', 'Subject': 'docindex3', 'Record Source': 'docindex4', 'Book Record': 'docindex5', 'Page': 'docindex6', 'Date': 'docindex7', 'Comments': 'docindex8', 'Instrument': 'docindex9', 'Status': 'docindex10', 'Owner': 'docindex11', 'Dates before 1753': 'docindex12'}
    }

    if job_name == 'HR':
        doc_model = PvdmDocs15
    elif job_name == 'Historic Order Books':
        doc_model = PvdmDocs113
    elif job_name == 'Historic Index Cards':
        doc_model = PvdmDocs114
    else:
        print("Invalid section name:", job_name)
        return

    obj = doc_model.objects.get(batchid=batchid)
    second_dict = model_to_dict(obj)

    first_dict = field_to_column_mapping.get(job_name)

    new_dict = {}
    for key, value in first_dict.items():
        if value in second_dict:
            new_dict[key] = second_dict.get(
                value, '') if second_dict.get(value) is not None else ''
            

    if 'Date' in new_dict:
        del new_dict['Date']

    return new_dict


# view image THAT WE SAVED IN INCOMPLETE BATCHES WE ENTERED LAST TIME( SAME LOGIC AS SERACH)
def view_image(jobid, batchid):

    job_name = PvcapJob1.objects.get(jobid=jobid).name

    if job_name == 'HR':
        obj_model = PvdmObjs15
        doc_model = PvdmDocs15
    elif job_name == 'Historic Order Books':
        obj_model = PvdmObjs113
        doc_model = PvdmDocs113
    elif job_name == 'Historic Index Cards':
        obj_model = PvdmObjs114
        doc_model = PvdmDocs114
    else:
        print("Invalid section name:", job_name)
        return

    docid = doc_model.objects.get(batchid=batchid).docid

    images = obj_model.objects.filter(docid=docid)
    images_data = []

    for image in images:
        dg_id = image.dgid
        dg_query = PvdmDg1.objects.filter(dgid=dg_id).first()
        if dg_query:
            filelist = image.filelist
            filenames = extract_filenames_base(filelist)

            for filename in filenames:
                if filename.isdigit() and len(filename) == 8:
                    path = os.path.join(
                        dg_query.path + dg_query.origdgname + '/IMG1/00000/', filename + '.TIF')
                else:
                    path = os.path.join(dg_query.path, filename)
                try:
                    with Image.open(path) as img:
                        output = io.BytesIO()
                        img.convert("RGB").save(output, format="JPEG")
                        image_data = base64.b64encode(
                            output.getvalue()).decode('utf-8')
                        images_data.append(image_data)
                except FileNotFoundError:
                    pass

    return images_data


def extract_filenames_base(filelist):
    if '<PATH>' in filelist:
        return extract_filenames_path_pattern(filelist)
    elif "Images" in filelist:
        return extract_filenames_extension_pattern(filelist)
    elif len(filelist) % 8 == 0 and all(char.isdigit() for char in filelist):
        return extract_filenames_byts_pattern(filelist)

    else:
        raise ValueError("Filelist does not match any known pattern")


def extract_filenames_byts_pattern(filelist):
    filenames = [filelist[i:i+8] for i in range(0, len(filelist), 8)]
    return filenames


def extract_filenames_extension_pattern(filelist):
    filenames = []
    current_filename = ''
    pattern_prefix = 'Images'

    for char in filelist:
        current_filename += char

        if current_filename.endswith(pattern_prefix):
            image_filename = current_filename[:-len(pattern_prefix)].strip()
            if image_filename:
                filenames.append(image_filename)
            current_filename = pattern_prefix

    if current_filename and current_filename != pattern_prefix:
        filenames.append(current_filename.strip())

    return filenames


def extract_filenames_path_pattern(filelist):
    pattern = re.compile(r'<PATH>(.*?)</PATH>')
    return pattern.findall(filelist)

# UPDATE DATA IN DOCS TABLE
def update_docs(job_id, updated_dict, batchid, status):

    section_name = PvcapJob1.objects.get(jobid=job_id).name

    if section_name == 'HR':
        table_model = PvdmDocs15
    elif section_name == 'Historic Order Books':
        table_model = PvdmDocs113
    elif section_name == 'Historic Index Cards':
        table_model = PvdmDocs114
    else:
        return None

    column_mapping = map_fields_to_columns(job_id)

    try:
        instance = table_model.objects.get(batchid=batchid)
    except table_model.DoesNotExist:
        return None

    for fieldname, value in updated_dict.items():
        column_name = column_mapping.get(fieldname)

        if column_name:
            if 'date' in column_name.lower():
                if not value:
                    value = None
                try:
                    value = datetime.strptime(value, '%Y-%m-%d')
                except ValueError as ve:
                    value = None
            setattr(instance, column_name.lower(), value)

    try:
        instance.save()  
    except ValidationError as ve:
        return None
    
    

    batch = PvcapBatch1.objects.get(batchid=batchid)

    if status == 'complete':
        batch.iscomplete = True
    elif status == 'incomplete':
        batch.iscomplete = False
    batch.save()

    try:
        instance.save()

    except ValidationError as ve:
        return None



