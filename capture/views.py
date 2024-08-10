from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .utils import*
from django.utils import timezone
from users.decorators import roles_required 
from django.contrib.auth.decorators import login_required
from users.models import PvdmUsers1

# Create your views here.


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
        
        save_form_data(job_id, form_data, status, batch_id)
        
        section_name = PvcapJob1.objects.filter(jobid=job_id).values_list('name', flat=True).first()

        dg_id = create_path(section_name)
        
        if section_name in ['HR', 'Historic Order Books', 'Historic Index Cards']:
            docid = save_field_data(form_data, job_id, dg_id)
        else:
            docid = None
        
        if docid is None:
            return JsonResponse({'error': 'Failed to save field data'}, status=400)
        
        uploaded_images = request.session.get('uploaded_images', [])
        print('uploaded images are:', upload_images)
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
            
        
        
        request.session.pop('uploaded_images', None)
        request.session.pop('image_count', None)

        
        return redirect('newBatch')
    
    context = {
            'fields' : fields,
            'uploaded_images' : uploaded_images,
            'section_name' : section_name,
            'user_role': user_role
        }
    
    return render(request, 'capture/create-batch.html', context)




@login_required
@csrf_exempt
def upload_images(request):
    print('Triggered################################')
    username = os.getlogin()
    print("username+++", username)
    uploaded_file_urls = []
    if request.method == 'POST' and request.FILES.getlist('images'):
        images = request.FILES.getlist('images')
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)

        for image in images:
            try:
                if image.name.lower().endswith('.tif'):
                    print('images is tiff')
                    image_contents = convert_image_to_jpg(image)
                    print('convert_image_to_jpg')
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
        # print('len is:', )

    return JsonResponse({'uploaded_images': uploaded_file_urls})



@login_required
@csrf_exempt
def upload_scanned_images(request):
    # folder_path = 'D:\\Pics\\egypt\\egypt' 
    # uploaded_file_urls = []
    # print('triggered')

    username = os.getlogin()
    print("username________________", username )
    # folder_path = f'C:\\Users\\{username}\\Documents\\Scanned Documents' 
    folder_path = f'C:\\Users\\{username}\\Downloads\\pics' 
    print("folder_path________________", folder_path )
    uploaded_file_urls = []
    print('triggered')
    print('dirs are:',os.listdir(folder_path))
    
    print(f"Checking folder path: {folder_path}")
    if not os.path.exists(folder_path):
        print(f"Folder does not exist: {folder_path}")
        return JsonResponse({'error': 'Scanned images folder does not exist'}, status=400)
    
    print(f"Folder exists: {folder_path}")
    for filename in os.listdir(folder_path):
        print(f"Found file: {filename}")
        if filename.strip().lower().endswith(('.png', '.jpg', '.jpeg', '.tif', '.tiff')):
            file_path = os.path.join(folder_path, filename)
            print(f"Processing file: {file_path}")
            fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT))
            saved_filename = fs.save(filename, open(file_path, 'rb'))
            uploaded_file_urls.append(fs.url(saved_filename))
            os.remove(file_path)
            print(f"Saved and removed file: {file_path}")
    
    if 'uploaded_images' not in request.session:
        request.session['uploaded_images'] = []
    request.session['uploaded_images'].extend(uploaded_file_urls)

    if 'image_count' not in request.session:
        request.session['image_count'] = 0
    request.session['image_count'] += len(uploaded_file_urls)
    print('images length in the session is:', request.session['image_count'])

    return JsonResponse({'uploaded_images': uploaded_file_urls})


@login_required
@csrf_exempt
def delete_image(request):
    if request.method == 'POST':
        print("Received POST request")
        print("Request data:", request.POST)
        image_url = request.POST.get('deleteUrl')
        print("image_url:", image_url)
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




def capture(request):
    return render(request, 'capture/capture.html')


#function to create batch type
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
                path='no where',
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
            print('created')
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





@login_required
def incompleteBatch (request):

    login_user = PvdmUsers1.objects.get(user=request.user).userid
    
    incomplete_batches = PvcapBatch1.objects.filter(iscomplete=False, userid=login_user)

    resultCount = incomplete_batches.count()


    context = {'incomplete_batches': incomplete_batches,
               'resultCount': resultCount}


    return render(request , 'capture/incomplete-batches.html', context)