from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .utils import *
from django.utils import timezone
from users.decorators import roles_required
from django.contrib.auth.decorators import login_required
from users.models import PvdmUsers1
from batches.models import *
from django.forms.models import model_to_dict


# Create your BATCH ALL CYCLE INCLUDING HELPER FUNCTIONS AFTER IT IS COMPLETED IT REMOVE IMAGED IN MEDIS AND IMAGES URL IN SESSIONS.
@login_required
@csrf_exempt
def create_batch(request):
    batch_id = None
    if request.method == 'POST':
        job_id = request.POST.get('job_id')
        batch_id = request.POST.get('batch_id')
        fields, index_ids, job_id = get_job_data(job_id)
        form_data = {field: request.POST.get(field) for field in fields}
        status = 'complete' if 'complete' in request.POST else 'incomplete'


        try:
            login_user = PvdmUsers1.objects.get(user=request.user)
            user_role = login_user.role.name
        except PvdmUsers1.DoesNotExist:
            user_role = None

        if status == 'incomplete':
            request.session.pop('uploaded_images', None)
            request.session.pop('image_count', None)
            return redirect('incompleteBatch')

        try:
            fields_with_index_ids = PvcapIndex1.objects.filter(
                jobid=job_id).values_list('indexid', 'fieldname')
            index_id_map = {fieldname: indexid for indexid,
                            fieldname in fields_with_index_ids}
            create_last_bundle(batch_id, job_id, form_data)
            bundles = PvcapBundle.objects.filter(batchid=batch_id)
            bundles_ids = [bundle.bundleid for bundle in bundles]

            bundle_data = {}
            for bundleid in bundles_ids:
                # indexibg bundleid in indexvalue table to enhance performance
                rows = PvcapIndexvalue1.objects.filter(bundleid=bundleid)
                bundle_data = {row.indexid: row.value for row in rows}
                result = {}
              
                for fieldname, indexid in index_id_map.items():
                    
                    result[fieldname] = bundle_data.get(indexid, '')


                section_name = PvcapJob1.objects.get(jobid=job_id).name
                dgid = create_path(section_name)

                if section_name in ['HR', 'Historic Order Books', 'Historic Index Cards']:
                    docid = save_field_data(result, job_id, dgid, batch_id)
                else:
                    docid = None

                if docid is None:
                    return JsonResponse({'error': 'Failed to save field data'}, status=400)

                save_bundle_image_names_to_database(
                    docid, section_name, batch_id, bundleid, dgid)

            batch = PvcapBatch1.objects.get(batchid=batch_id)

            if status is not None:
                if status == 'complete':
                    batch.iscomplete = True
                elif status == 'incomplete':
                    batch.iscomplete = False
                batch.save()

            delete_batch_dir(batch_id)
            request.session.pop('uploaded_images', None)
            request.session.pop('image_count', None)

        except Exception as e:
            uploaded_images = request.session.get('uploaded_images', [])
            delete_batch_dir(batch_id)
            request.session.pop('uploaded_images', None)
            request.session.pop('image_count', None)
            return JsonResponse({'error': str(e)}, status=400)

        return redirect('newBatch')
    
    batch_id_from_session = request.session.get('batch_id', None)

    context = {
        'fields': fields,
        'result': result,
        'images': uploaded_images,
        'section_name': section_name,
        'user_role': user_role,
        'batchid': batch_id if batch_id else batch_id_from_session
    }

    return render(request, 'capture/create-batch.html', context)


# SERVER UPLOAD IMAGE AND SAVE PHYICAL IMAGES IN MEDIA DIRCTORY AND IMAGES URL IN SESSIONS in settings(media url= '')
@login_required
@csrf_exempt
def upload_images(request):
    username = os.getlogin()
    uploaded_file_urls = []
    if request.method == 'POST' and request.FILES.getlist('images'):
        images = request.FILES.getlist('images')
        batchid = request.POST.get('batch_id')
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)

        for image in images:
            try:
                if image.name.lower().endswith('.tif'):
                    image_contents = convert_image_to_jpg(image)
                    base_filename = os.path.splitext(image.name)[0]

                    for i, img_content in enumerate(image_contents):
                        filename = f"{base_filename}_page_{i+1}.jpg"
                        fs.save(filename, ContentFile(img_content))
                        uploaded_file_urls.append(fs.url(filename))
                else:
                    filename = image.name
                    fs.save(filename, image)
                    uploaded_file_urls.append(fs.url(filename))

            except Exception as e:
                print(f"Error saving file {image.name}: {e}")

        if 'uploaded_images' not in request.session:
            request.session['uploaded_images'] = []
        request.session['uploaded_images'].extend(uploaded_file_urls)

        if 'image_count' not in request.session:
            request.session['image_count'] = 0
        request.session['image_count'] += len(images)

    return JsonResponse({'uploaded_images': uploaded_file_urls})


# accesss folder path dir and get images to media dir and save images url in session then delete images from folder path
@login_required
@csrf_exempt
def upload_scanned_images(request):
    client_ip = get_client_ip(request)
    if not client_ip:
        return JsonResponse({'error': 'Unable to retrieve client IP address'}, status=400)

    username = os.getlogin()
    folder_path = rf'\\{client_ip}\iTrackFilesScan'
    uploaded_file_urls = []

    if not os.path.exists(folder_path):
        return JsonResponse({'error': 'Scanned images folder does not exist'}, status=400)

    for filename in os.listdir(folder_path):
        if filename.strip().lower().endswith(('.png', '.jpg', '.jpeg', '.tif', '.tiff')):
            file_path = os.path.join(folder_path, filename)
            fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT))

            if filename.lower().endswith(('.tif', '.tiff')):
                with open(file_path, 'rb') as image_file:
                    image_contents = convert_image_to_jpg(image_file)
                    base_filename = os.path.splitext(filename)[0]

                    for i, img_content in enumerate(image_contents):
                        saved_filename = f"{base_filename}_page_{i+1}.jpg"
                        fs.save(saved_filename, ContentFile(img_content))
                        uploaded_file_urls.append(fs.url(saved_filename))

            else:
                saved_filename = fs.save(filename, open(file_path, 'rb'))
                uploaded_file_urls.append(fs.url(saved_filename))
            os.remove(file_path)
    if 'uploaded_images' not in request.session:
        request.session['uploaded_images'] = []
    request.session['uploaded_images'].extend(uploaded_file_urls)

    if 'image_count' not in request.session:
        request.session['image_count'] = 0
    request.session['image_count'] += len(uploaded_file_urls)

    return JsonResponse({'uploaded_images': uploaded_file_urls})


# delete images from media amd url in session
@login_required
@csrf_exempt
def delete_image(request):
    if request.method == 'POST':
        data = json.loads(request.body)  
        image_name = data.get('imageName')
        batchid = data.get('batchid')
 
        
        uploaded_images = request.session.get('uploaded_images', [])

        if image_name in uploaded_images:
            uploaded_images.remove(image_name)
            request.session['uploaded_images'] = uploaded_images

        if batchid:
            image_path = os.path.join(
                settings.MEDIA_ROOT, f'batch_{batchid}', image_name
            )
        else:
            image_path = os.path.join(
                settings.MEDIA_ROOT, image_name
            )

        try:
            if os.path.exists(image_path):                 
                os.remove(image_path)
        except Exception as e:
            print(f"Error deleting image {image_path}: {e}")

        return JsonResponse({'success': True, 'uploaded_images': uploaded_images})


    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)


# render capture page
@login_required
@roles_required('hr_staff', 'hr_manager', 'historic_staff')
def capture(request):
    return render(request, 'capture/capture.html')


# function to create batch type ( HR, HIstoric index or orderbook) page
@login_required
def new_batch(request):

    if request.method == 'POST':
        job_name = request.POST.get('job')
        login_user = PvdmUsers1.objects.get(user=request.user).userid

        if not job_name:
            return render(request, 'capture/new-batch.html', {'error': 'Invalid job selected'})

        name = request.POST.get('name')
        date = request.POST.get('date')
        description = request.POST.get('description')

        job = get_object_or_404(PvcapJob1, name=job_name)
        job_id = job.jobid

        fields_with_index_ids = PvcapIndex1.objects.filter(
        jobid=job_id).values_list('indexid', 'fieldname')
        index_id_map = {fieldname: indexid for indexid,
                    fieldname in fields_with_index_ids}

        result = {key: "" for key in index_id_map}

        try:
            job = get_object_or_404(PvcapJob1, name=job_name)
            job_id = job.jobid
        except PvcapJob1.DoesNotExist:
            return render(request, 'capture/new-batch.html', {'error': 'Job not found'})

        try:
            login_user = PvdmUsers1.objects.get(user=request.user)
            login_user_id = PvdmUsers1.objects.get(user=request.user).userid
            user_role = login_user.role.name
        except PvdmUsers1.DoesNotExist:
            user_role = None

        try:
            batch = PvcapBatch1.objects.create(
                name=name,
                userdate=date,
                description=description,
                jobid=job_id,
                path='handled',
                isdeleted=False,
                isnew=True,
                retainstats=0,
                adminpriority=0,
                status=2,
                jobstart=timezone.now(),
                stepid=1,
                stepstart=timezone.now(),
                size=0,
                lastupdate=timezone.now(),
                userid=login_user_id
            )
        except Exception as e:
            return render(request, 'capture/new-batch.html', {'error': 'Error creating batch'})

        fields, indexids, job_id = get_job_data(job_id)


        bundles = PvcapBundle.objects.filter(batchid=batch.batchid)
        first_bundle = bundles.first() if bundles.exists() else None
        bundleid = first_bundle.bundleid if first_bundle else None
        bundles_ids = [
        bundle.bundleid for bundle in bundles if bundle.submit is False]
        bundle_count = len(bundles)

        batch_dir = os.path.join(settings.MEDIA_ROOT, f'batch_{batch.batchid}')

        is_bundled = True

        if os.path.exists(batch_dir):
            images = [f for f in os.listdir(
                batch_dir) if os.path.isfile(os.path.join(batch_dir, f))]
            is_bundled = False
        else:
            images = []

        context = {
                   'result': result,
                   'batchid': batch.batchid,
                   'jobid': job_id,
                   'indexids': indexids,
                   'user_role': user_role,
                   'media_url': settings.MEDIA_URL,
                   'bundleid': bundleid,
                   'bundle_count': bundle_count,
                   'bundles_ids': bundles_ids,
                   'is_bundled': is_bundled
                    }

        return render(request, 'capture/create-batch.html', context)

    try:
        login_user = PvdmUsers1.objects.get(user=request.user)
        user_role = login_user.role.name

    except PvdmUsers1.DoesNotExist:
        user_role = None

    context = {
        'user_role': user_role
    }

    return render(request, 'capture/new-batch.html', context)


# render incomplete batches
@login_required
def incomplete_batch_list(request):

    login_user = PvdmUsers1.objects.get(user=request.user).userid
    incomplete_batches = PvcapBatch1.objects.filter(
        iscomplete=False, userid=login_user)
    resultCount = incomplete_batches.count()
    context = {'incomplete_batches': incomplete_batches,
               'resultCount': resultCount}

    return render(request, 'capture/incomplete-batches.html', context)


# work when we click on one of the rows of incomplete batch
@login_required
@csrf_exempt
def update_batch(request, pk):

    login_user = PvdmUsers1.objects.get(user=request.user)
    user_role = login_user.role.name
    batch = PvcapBatch1.objects.get(pk=pk)
    batchid = batch.batchid
    jobid = batch.jobid

    if 'incomplete' in request.POST:

        return redirect('incompleteBatch')

    if 'complete' in request.POST:
        form_data = request.POST.dict()
        form_data.pop('csrfmiddlewaretoken', None)

        batch_id = form_data.pop('batch_id', None)

        job_id = form_data.pop('job_id', None)
        bundleid = form_data.pop('bundle_id', None)
        current_image = form_data.pop('imageName', None)
        batch.iscomplete = True
        batch.save()

        if bundleid == 'null':
            bundleid = None

        images = []

        if bundleid is None:
            try:
                bundle = PvcapBundle.objects.create(
                    batchid=batch_id,
                    createdate=datetime.now()
                )
                bundleid = bundle.bundleid
            except Exception as e:
                return JsonResponse({'error': 'Failed to create bundle'}, status=500)

            upload_images = request.session.get('uploaded_images')

            save_bundle_images(batch_id, bundle.bundleid,
                               upload_images, current_image)
            save_bundle_form_data(job_id, form_data, batch_id, bundle.bundleid)

            batch_dir = os.path.join(settings.MEDIA_ROOT, f'batch_{batch_id}')
            section_name = PvcapJob1.objects.get(jobid=job_id).name
            dgid = create_path(section_name)

            if section_name in ['HR', 'Historic Order Books', 'Historic Index Cards']:
                docid = save_field_data(form_data, job_id, dgid, batch_id)
            else:
                docid = None

            if docid is None:
                return JsonResponse({'error': 'Failed to save field data'}, status=400)

            save_bundle_image_names_to_database(
                docid, section_name, batch_id, bundleid, dgid)

            try:
                bundle = PvcapBundle.objects.get(bundleid=bundleid)
                bundle.submit = True
                bundle.save()
            except ObjectDoesNotExist:
                return JsonResponse({'error': 'Bundle ID does not exist'}, status=404)


            delete_batch_dir(batch_id)

            return redirect('newBatch')
            

    bundles = PvcapBundle.objects.filter(batchid=batchid)
    first_bundle = bundles.first() if bundles.exists() else None
    bundleid = first_bundle.bundleid
    bundles_ids = [
        bundle.bundleid for bundle in bundles if bundle.submit is False]
    bundle_count = len(bundles)

    batch_dir = os.path.join(settings.MEDIA_ROOT, f'batch_{batchid}')

    is_bundled = True

    if os.path.exists(batch_dir):
        images = [f for f in os.listdir(
            batch_dir) if os.path.isfile(os.path.join(batch_dir, f))]
        is_bundled = False
    else:
        images = []

    fields_with_index_ids = PvcapIndex1.objects.filter(
        jobid=jobid).values_list('indexid', 'fieldname')
    index_id_map = {fieldname: indexid for indexid,
                    fieldname in fields_with_index_ids}

    result = {key: "" for key in index_id_map}

    context = {
        'batchid': batchid,
        'jobid': jobid,
        'user_role': user_role,
        'bundleid': bundleid,
        'bundle_count': bundle_count,
        'bundles_ids': bundles_ids,
        'is_bundled': is_bundled,
        'result': result,
        'images': images,
        'media_url': settings.MEDIA_URL,
    }

    return render(request, 'capture/update-batch.html', context)


@login_required
@csrf_exempt
def create_bundle(request):
    if request.method == 'POST':
        try:
            form_data = request.POST.dict()
            form_data.pop('csrfmiddlewaretoken', None)

            current_image = form_data.pop('imageName', None)
            batch_id = form_data.pop('batch_id', None)
            job_id = form_data.pop('job_id', None)

            try:
                bundle = PvcapBundle.objects.create(
                    batchid=batch_id,
                    createdate=datetime.now()
                )
            except Exception as e:
                print('exception is:', e)

            upload_images = request.session.get('uploaded_images')

            save_bundle_images(batch_id, bundle.bundleid,
                               upload_images, current_image)

            save_bundle_form_data(job_id, form_data, batch_id, bundle.bundleid)

            bundle_id = bundle.batchid
            bundles = PvcapBundle.objects.filter(batchid=batch_id)
            bundle_ids = [
                bundle.bundleid for bundle in bundles if bundle.submit is False]

            batch_dir = os.path.join(settings.MEDIA_ROOT, f'batch_{batch_id}')

            if os.path.exists(batch_dir):
                images = [f for f in os.listdir(
                    batch_dir) if os.path.isfile(os.path.join(batch_dir, f))]

            response_data = {
                'success': True,
                'message': 'Data received successfully',
                'form_data': form_data,
                'current_image': current_image,
                'bundle_id': bundle_id,
                'batch_id': batch_id,
                'bundle_ids': bundle_ids,
                'unbundled_images': images,
                'media_url': settings.MEDIA_URL
            }

            return JsonResponse(response_data)

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})


@csrf_exempt
def get_bundle_data(request, bundleid, batchid):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            bundleid = data.get('bundle_id')
            batchid = data.get('batch_id')

            if not batchid:
                return JsonResponse({'error': 'Missing batchid'}, status=400)

            if bundleid:
                bundle_dir = os.path.join(settings.MEDIA_ROOT, f'batch_{batchid}', f'bundle_{bundleid}')
            else:
                bundle_dir = os.path.join(
                    settings.MEDIA_ROOT, f'batch_{batchid}')

            images = [f for f in os.listdir(bundle_dir) if os.path.isfile(
                os.path.join(bundle_dir, f))] if os.path.exists(bundle_dir) else []

            if bundleid:
                batch = get_object_or_404(PvcapBatch1, batchid=batchid)
                jobid = batch.jobid

                fields_with_index_ids = PvcapIndex1.objects.filter(
                    jobid=jobid).values_list('indexid', 'fieldname')
                index_id_map = {fieldname: indexid for indexid,
                                fieldname in fields_with_index_ids}
                # same as in  row 49
                rows = PvcapIndexvalue1.objects.filter(bundleid=bundleid)
                bundle_data = {row.indexid: row.value for row in rows}

                result = {}
                for fieldname, indexid in index_id_map.items():
                    result[fieldname] = bundle_data.get(indexid, '')
            else:
                result = {}

            return JsonResponse({
                'images': images,
                'result': result,
                'media_url': settings.MEDIA_URL,
                'batchid': batchid
            })
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)


# function to submit bundles
def submit_bundle(request):
    if request.method == 'POST':
        try:
            form_data = request.POST.dict()
            form_data.pop('csrfmiddlewaretoken', None)

            batch_id = form_data.pop('batch_id', None)
            job_id = form_data.pop('job_id', None)
            bundleid = form_data.pop('bundle_id', None)
            current_image = form_data.pop('imageName', None)

            if bundleid == 'null':
                bundleid = None

            images = []

            if bundleid is None:
                try:
                    bundle = PvcapBundle.objects.create(
                        batchid=batch_id,
                        createdate=datetime.now()
                    )
                    bundleid = bundle.bundleid
                except Exception as e:
                    return JsonResponse({'error': 'Failed to create bundle'}, status=500)

                upload_images = request.session.get('uploaded_images')

                save_bundle_images(batch_id, bundle.bundleid,
                                   upload_images, current_image)
                save_bundle_form_data(
                    job_id, form_data, batch_id, bundle.bundleid)

                batch_dir = os.path.join(
                    settings.MEDIA_ROOT, f'batch_{batch_id}')
                if os.path.exists(batch_dir):
                    images = [f for f in os.listdir(
                        batch_dir) if os.path.isfile(os.path.join(batch_dir, f))]

            section_name = PvcapJob1.objects.get(jobid=job_id).name
            dgid = create_path(section_name)

            if section_name in ['HR', 'Historic Order Books', 'Historic Index Cards']:
                docid = save_field_data(form_data, job_id, dgid, batch_id)
            else:
                docid = None

            if docid is None:
                return JsonResponse({'error': 'Failed to save field data'}, status=400)

            save_bundle_image_names_to_database(
                docid, section_name, batch_id, bundleid, dgid)

            try:
                bundle = PvcapBundle.objects.get(bundleid=bundleid)
                bundle.submit = True
                bundle.save()
            except ObjectDoesNotExist:
                return JsonResponse({'error': 'Bundle ID does not exist'}, status=404)

            return JsonResponse({
                'status': 'success',
                'message': 'Form submitted successfully!',
                'bundleid': bundleid,
                'unbundled_images': images,
                'batch_id': batch_id,
                'media_url': settings.MEDIA_URL
            })

        except ObjectDoesNotExist as e:
            return JsonResponse({'error': 'Job ID does not exist'}, status=404)

        except Exception as e:
            return JsonResponse({'error': 'An unexpected error occurred'}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
