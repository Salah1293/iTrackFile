from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .utils import*
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
        try:

            save_form_data(job_id, form_data, status, batch_id)
            
            section_name = PvcapJob1.objects.filter(jobid=job_id).values_list('name', flat=True).first()

            dg_id = create_path(section_name)
            
            if section_name in ['HR', 'Historic Order Books', 'Historic Index Cards']:
                docid = save_field_data(form_data, job_id, dg_id, batch_id)
            else:
                docid = None
            
            if docid is None:
                return JsonResponse({'error': 'Failed to save field data'}, status=400)
            
            uploaded_images = request.session.get('uploaded_images', [])
            image_count = len(uploaded_images)
            
            if not uploaded_images:
                return JsonResponse({'error': 'No uploaded images found'}, status=400)
            
            save_image_names_to_database(docid, uploaded_images, section_name, image_count, batch_id, dg_id)

            for image_url in uploaded_images:
                image_path = os.path.join(settings.MEDIA_ROOT, image_url.lstrip('/media/'))
                try:
                    if os.path.exists(image_path):
                        os.remove(image_path)
                except Exception as e:
                    print(f"Error deleting image {image_path}: {e}")
                
            

            delete_images(uploaded_images)
            
            request.session.pop('uploaded_images', None)
            request.session.pop('image_count', None)

        except Exception as e:
            uploaded_images = request.session.get('uploaded_images', [])
            delete_images(uploaded_images)
            request.session.pop('uploaded_images', None)
            request.session.pop('image_count', None)
            return JsonResponse({'error': str(e)}, status=400)
        

    
        return redirect('newBatch')
    
    context = {
            'fields' : fields,
            'uploaded_images' : uploaded_images,
            'section_name' : section_name,
            'user_role': user_role
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
    username = os.getlogin()
    # folder_path = f'C:\\iTrackFilesScan' 
    folder_path = f'C:\\Users\\{username}\\Downloads\\pics' 
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
            print("removeddddddddddddddd")
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
        image_url = request.POST.get('deleteUrl')
        image_url = request.POST.get('deleteUrl')
        uploaded_images = request.session.get('uploaded_images', [])

        if image_url in uploaded_images:
            uploaded_images.remove(image_url)
            request.session['uploaded_images'] = uploaded_images

            image_path = os.path.join(settings.MEDIA_ROOT, image_url.lstrip('/'))
            try:
                if os.path.exists(image_path):
                    os.remove(image_path)
            except Exception as e:
                print(f"Error deleting image {image_path}: {e}")

            return JsonResponse({'success': True, 'uploaded_images': uploaded_images})

        return JsonResponse({'success': False, 'error': 'Image not found in session'}, status=400)

    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)


# render capture page
@login_required
@roles_required('hr_staff', 'hr_manager', 'historic_staff')
def capture(request):
    return render(request, 'capture/capture.html')


#function to create batch type ( HR, HIstoric index or orderbook) page
@login_required
def new_batch(request):

    if request.method == 'POST':
        job_name = request.POST.get('job')
        login_user = PvdmUsers1.objects.get(user=request.user).userid

        if not job_name:
            return render(request, 'capture/new-batch.html', {'error' : 'Invalid job selected'})

        name = request.POST.get('name')
        date = request.POST.get('date')
        description = request.POST.get('description')



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


        context = {'fields' : fields, 'batchid': batch.batchid,
                    'jobid': job_id, 'indexids': indexids,
                     'user_role': user_role }


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
def incomplete_batch_list (request):

    login_user = PvdmUsers1.objects.get(user=request.user).userid
    
    incomplete_batches = PvcapBatch1.objects.filter(iscomplete=False, userid=login_user)

    resultCount = incomplete_batches.count()


    context = {'incomplete_batches': incomplete_batches,
               'resultCount': resultCount}


    return render(request , 'capture/incomplete-batches.html', context)

# work when we click on one of the rows of incomplete batch
@login_required
@csrf_exempt
def update_batch(request, pk):

    login_user = PvdmUsers1.objects.get(user=request.user)
    user_role = login_user.role.name
    batch = PvcapBatch1.objects.get(pk=pk)
    batchid = batch.batchid
    jobid = batch.jobid
    new_dict = fields_conversion(batchid, jobid)

    image_data = view_image(jobid, batchid)

    if request.method == 'POST':
       
        batchid = request.POST.get('batch_id', batchid)
        jobid = request.POST.get('job_id', jobid)
        status = 'complete' if 'complete' in request.POST else 'incomplete' 
        updated_dict = {field: request.POST.get(field, value) for field, value in new_dict.items()}
        
        update_docs(jobid, updated_dict, batchid, status)
        if not jobid:
            return HttpResponse("Job ID is missing or invalid", status=400)

        return redirect('newBatch')
    
    context = {'new_dict': new_dict,
        'batchid': batchid,
        'jobid': jobid,
        'image_data': image_data,
        'user_role': user_role,
        }
    
    return render(request, 'capture/update-batch.html', context)