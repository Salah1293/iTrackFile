from django import forms
from django.contrib.auth.models import User
from .models import PvdmUsers1, Role
from django.db import IntegrityError

class UserCreationForm(forms.ModelForm):
    role = forms.ModelChoiceField(queryset=Role.objects.all(), required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = PvdmUsers1
        fields = ['username', 'fullname', 'email', 'password', 'role']

    email = forms.EmailField(required=False)

    def save(self, commit=True):
        pvdm_user = super().save(commit=False)
        username = self.cleaned_data['username']
        raw_password = self.cleaned_data['password']
        
        user, created = User.objects.get_or_create(
            username=username,
            defaults={'email': self.cleaned_data.get('email', '')}
        )
        
        if not created:
            raise IntegrityError('User with this username already exists.')
        
        user.set_password(raw_password)  
        user.save()
        
        pvdm_user.user = user
        pvdm_user.isdeleted = False
        
        if commit:
            pvdm_user.save()
        
        return pvdm_user



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = PvdmUsers1
        fields = ['username', 'fullname', 'email', 'role']



class UserUpdateSelfForm(forms.ModelForm):
    class Meta:
        model = PvdmUsers1
        fields = ['username', 'fullname', 'email', 'password']

