from django.contrib import admin
from UserInformation.models import *


class UserInformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'age', 'weight')


# Register your models here.
admin.site.register(UserInformation, UserInformationAdmin)
admin.site.register(UserType)
