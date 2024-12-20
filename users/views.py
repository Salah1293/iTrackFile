from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages import error
from django.contrib.auth.decorators import login_required
from users.decorators import roles_required 
from batches.utils import paginate
from django.contrib.auth.decorators import user_passes_test
from .forms import *
from django.db import IntegrityError
from django.urls import reverse

# Create your views here.



#login function based view
def loginUser(request):

    if request.user.is_authenticated:
        return redirect('landingBatches')
    
    if request.method == 'POST':

        username = request.POST['username'].lower()
        password = request.POST['password']


        try:
            user = User.objects.get(username=username)
            pvdm_user = PvdmUsers1.objects.get(user=user)
            if pvdm_user.isdeleted or not user.is_active:
                messages.error(request, 'This account has been deleted or deactivated.')
                return redirect('login')
        except (User.DoesNotExist, PvdmUsers1.DoesNotExist):
            messages.error(request, 'Username does not exist')
            return redirect('login')


        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', 'landingBatches'))
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'users/login.html')


#logout function based view
def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('login')


@login_required
def update_user_self(request):
    login_user = get_object_or_404(PvdmUsers1, username=request.user)
    user = login_user.user

    if request.method == 'POST':
        form = UserUpdateSelfForm(request.POST, instance=login_user)
        if form.is_valid():
            try:      
                if (form.cleaned_data.get('password') or
                     form.cleaned_data.get('username') or
                     form.cleaned_data.get('fullname') or
                     form.cleaned_data.get('email')):
                    new_password = form.cleaned_data.get('password')
                    login_user.username = form.cleaned_data.get('username')
                    login_user.fullname = form.cleaned_data.get('fullname')
                    login_user.email = form.cleaned_data.get('email')
                    login_user.password = new_password
                    user.set_password(new_password)


                user.save()
                login_user.save()
                form.save()

                return redirect('managing')
            except IntegrityError:
                messages.error(request, 'An error happens while updating.')
        else:
            messages.error(request, 'Form is mot Valid.')

    else:
        form = UserUpdateSelfForm(instance=login_user)


    return render(request, 'users/update-profile.html', {'form': form})


@login_required
@roles_required('admin')
def user_list(request):
    users = PvdmUsers1.objects.filter(isdeleted=False)
    resultCount = users.count()
    custom_range, users = paginate(request, users)
    context = {
        'users': users,
        'resultCount': resultCount,
        'custom_range': custom_range
    }
    return render(request, 'users/user-list.html', context)



@login_required
@roles_required('admin')
def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'User created successfully.')
                return redirect('userList')
            except IntegrityError as e:
                form.add_error(None, 'User with this username already exists.')
        else:
            messages.error(request, 'Form is not valid. Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'users/create-user.html', {'form': form})


@login_required
@roles_required('admin')
def delete_user(request, user_id):
    try:
        pvdm_user = PvdmUsers1.objects.get(userid=user_id)
        pvdm_user.isdeleted = True
        pvdm_user.save()

        user = pvdm_user.user
        user.is_active = False
        user.isdeleted = True  
        user.save()

        messages.success(request, 'User deleted successfully.')
    except PvdmUsers1.DoesNotExist:
        messages.error(request, 'User does not exist.')

    return redirect('userList')



@login_required
@roles_required('admin')
def update_user(request, user_id):
    pvdm_user = get_object_or_404(PvdmUsers1, pk=user_id)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=pvdm_user)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'User updated successfully.')
                return redirect('userList')
            except IntegrityError:
                messages.error(request, 'An error occurred while updating the user. Please try again.')
        else:
            messages.error(request, 'Form is not valid. Please correct the errors below.')
    else:
        form = UserUpdateForm(instance=pvdm_user)

    return render(request, 'users/create-user.html', {'form': form})



def myAdmin(request):

    return render(request, 'users/admin.html')




# render admin operation page
@login_required(login_url='login')
def managing(request):
 

    return render(request, 'users/managing.html')



# @login_required(login_url='login')
def help_app(request):

    return render(request, 'users/help.html')


def myUser(request):

    return render(request, 'users/user.html')



@login_required
@roles_required('admin')
def reset_user_password(request, user_id):
    try:
        pvdm_user = PvdmUsers1.objects.get(pk=user_id)     
        user = pvdm_user.user
        new_password = pvdm_user.username
        pvdm_user.password = pvdm_user.username
        user.set_password(new_password)
        user.save()
        pvdm_user.save()

        messages.success(request, f"Password for {pvdm_user.username} has been reset to the username.")
    except PvdmUsers1.DoesNotExist:
        messages.error(request, 'User does not exist.')

    return redirect('userList')