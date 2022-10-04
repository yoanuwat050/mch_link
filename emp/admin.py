from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
from .models import *


admin.site.register(EmpUser),





class EmpUserInline(admin.StackedInline):
    model = EmpUser
    can_delete = False
    verbose_name_plural = 'empUser'


class UserAdmin(BaseUserAdmin):
    inlines = (EmpUserInline,)

admin.site.unregister(User),
admin.site.register(User, UserAdmin)