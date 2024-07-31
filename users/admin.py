from django.contrib import admin

# users/admin.py
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import PvdmUsers1

class PvdmUsers1Inline(admin.StackedInline):
    model = PvdmUsers1
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (PvdmUsers1Inline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(PvdmUsers1)

