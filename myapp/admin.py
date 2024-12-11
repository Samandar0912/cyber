from django.contrib import admin
from myapp.models import * 

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']  # ID va viloyat nomini ko'rsatadi
    list_display_links = ['id', 'title']


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('title', 'categoryRegion')  # Tuman nomi va Viloyatni ko'rsatish
    search_fields = ['title', 'categoryRegion__title']  # Viloyat va Tuman nomiga qarab qidirish imkoniyati


@admin.register(DeviceType)
class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']  # To‘g‘ri maydonni ishlating
    list_display_links = ['id', 'title']


@admin.register(UserDevice)
class UserDeviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'device_type'] 
    list_display_links = ['id', 'device_type']
    
    
@admin.register(DeviceStatistics)
class DeviceStatisticsAdmin(admin.ModelAdmin):
    list_display = ['id', 'category','device_count','lost_device_count'] 
    list_display_links = ['id', 'category']
    
    
@admin.register(UsersNote)
class UsersNoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','body'] 
    list_display_links = ['id', 'title']
    
    
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number'] 
    list_display_links = ['id', 'phone_number']


@admin.register(DeviceImei)
class DeviceImeiAdmin(admin.ModelAdmin):
    list_display = ['id', 'device','imei'] 
    list_display_links = ['id', 'device']


@admin.register(FoundDevice)
class FoundDeviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'imei','active_started','active_finished','operator','phone_number','is_viewed'] 
    list_display_links = ['id', 'imei','active_started']