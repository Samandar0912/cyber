from django.urls import path
from myapp.views import *

app_name = "main"
urlpatterns = [

    path('',login_user, name='login' ),
    path('logout/',logout_user, name='logout' ),

    path('Asosiy',index, name='index' ),
    path("Qurilmalar/",qurilma, name='qurilma' ),
    path("Ro'yxatlar/",table, name='table' ),
    path("Statistika/",statistika, name='statistika' ),
    
    path("Xodimlar/",users, name='users' ),
    path('user/update/<int:pk>/', update_user, name='update_user'),
    path('user/delate/<int:pk>/', delete_user, name='delete_user'),
    
    
    path("Malumotlar/",setting, name='setting' ),
    path("Malumotlar/Viloyat-kiritish",add_region, name='add_region' ),
    path("Malumotlar/Tuman-kiritish",add_district, name='add_district' ),
    path("Malumotlar/qurilma-turi",add_device_type, name='add_device_type' ),

    path('qurilma/update/<int:pk>/', update_qurilma, name='update_qurilma'),
    path('qurilma/delete/<int:pk>/', delete_table, name='delete_table'),
    
    
    path('district/update/<int:pk>/', update_district, name='update_district'),
    path('district/delete/<int:pk>/', delete_district, name='delete_district'),

    path('Device/update/<int:pk>/', update_device, name='update_device'),
    path('Device/delete/<int:pk>/', delete_device, name='delete_device'),

    path('Region/update/<int:pk>/', update_region, name='update_region'),
    path('Region/delete/<int:pk>/', delete_region, name='delete_region'),
    
    path('qurilma/add-note/', add_userNote, name='add_note'),
    path('qurilma/update-note/<int:pk>/', update_userNote, name='update_note'),
    path('qurilma/delate-note/<int:pk>/', delete_note, name='delete_note'),

    path("topilganlar/", found_device, name='founds' ),
    path('topilganlar/<int:pk>/', found_device_detail, name='found'),
    path('topilganlar/<int:pk>/delete/', delete_found_device, name='delete_found_device'),



]