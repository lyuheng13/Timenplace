from django.contrib import admin

from .models import Profile,Location,Cusine,newLocation


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user_id', 'id','user', 'date_of_birth', 'photo']

@admin.register(Location)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['DBA','BORO', 'BUILDING','STREET','ZIPCODE','PHONE','CUISINE','LATITUDE','LONGITUDE']


@admin.register(newLocation)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['DBA','BORO', 'BUILDING','STREET','ZIPCODE','PHONE','CUISINE','LATITUDE','LONGITUDE']

@admin.register(Cusine)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['cusine']
