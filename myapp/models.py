from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from .validators import validate_file_extension, validate_file_size
import re  
from django.contrib.auth.models import AbstractUser
    

def validate_imei(value):
    """IMEI raqami validatsiyasi: 15 raqam va faqat sonlardan iborat bo'lishi kerak."""
    if len(str(value)) != 15 or not str(value).isdigit():
        raise ValidationError("IMEI raqami 15 ta raqamdan iborat bo‘lishi kerak.")





def validate_phone_number(value):
    """Telefon raqamini tekshirish."""
    phone_regex = re.compile(r'^\+998\d{9}$')
    if not phone_regex.match(value):
        raise ValidationError("Telefon raqami +998 bilan boshlanishi va 12 ta raqam bo‘lishi kerak.")





class Region(models.Model):
    title = models.CharField(max_length=150, verbose_name="Viloyatlar")

    class Meta:
        verbose_name = "Viloyat nomi"
        verbose_name_plural = "Viloyat nomi"

    def __str__(self):
        return str(self.title)
    
class DeviceType(models.Model):
    title = models.CharField(max_length=150, verbose_name="Quqilma turi")
    
    class Meta:
        verbose_name = "Qurilma Turi"
        verbose_name_plural = "Qurilma Turi"
        
    def __str__(self):
        return str(self.title)
    
    
    
class District(models.Model):
    categoryRegion = models.ForeignKey(Region, verbose_name="Viloyat", on_delete=models.CASCADE, related_name='district')
    title = models.CharField(max_length=150, verbose_name="Tuman nomi")

    class Meta:
        verbose_name = "Tuman nomi"
        verbose_name_plural = "Tuman nomi"
        unique_together = ['categoryRegion', 'title']

    def __str__(self):
        return f"{self.title} ({self.categoryRegion.title})"




class UserDevice(models.Model):
    name = models.CharField(max_length=150, verbose_name="ism")
    categoryRegion = models.ForeignKey(Region, verbose_name="Viloyat", on_delete=models.CASCADE)
    categoryDistrict = models.ForeignKey(District, verbose_name="Tuman", on_delete=models.CASCADE)
    device_type = models.ForeignKey(DeviceType, verbose_name="qurilma turi", on_delete=models.CASCADE)
    
    device_name = models.CharField(max_length=100, verbose_name='qurilma nomi')
    data = models.DateTimeField(auto_now_add=False, verbose_name="Yo'qolgan Vaqti" )
    phone_number = models.CharField(max_length=13,validators=[validate_phone_number],verbose_name="Telefon raqami")
    
    file = models.FileField(upload_to='Media/', 
        validators=[validate_file_size, validate_file_extension],
        help_text="Fayl hajmi 5 MB dan oshmasligi va kengaytmasi .pdf bo‘lishi kerak.",verbose_name="ariza yuborish"
    )

    class Meta:
        verbose_name = "Qurilama nomi"
        verbose_name_plural = "Qurilama nomi"
    
    @property
    def get_imeis(self):
        return "\n".join(map(str, self.imeis.all()))

    def __str__(self):
        return self.name


  
class DeviceImei(models.Model):
    device = models.ForeignKey(UserDevice, on_delete=models.CASCADE, related_name='imeis')
    imei = models.CharField(max_length=15, validators=[validate_imei], unique=True, verbose_name="IMEI raqami")
    
    def __str__(self):
        return self.imei
    
  
   




class DeviceStatistics(models.Model):
    category = models.CharField(max_length=150, verbose_name="Kategoriya")
    device_count = models.IntegerField(verbose_name="Qurilma soni")
    lost_device_count = models.IntegerField(verbose_name="Yo'qolgan qurilmalar soni")

    class Meta:
        verbose_name = "Qurilma statistikasi"
        verbose_name_plural = "Qurilma statistikasi"

    def __str__(self):
        return f"{self.category} - {self.device_count} qurilma, {self.lost_device_count} yo'qolgan"



class Account(AbstractUser):
    phone_number = models.CharField(max_length=13,validators=[validate_phone_number],verbose_name="Telefon raqami")
    lavel = models.CharField(max_length=50, verbose_name="lavozimi")
    REQUIRED_FIELDS = []

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    
    
class UsersNote(models.Model):
    title = models.CharField(max_length=200, verbose_name='Sarlovha')
    body = models.TextField(verbose_name='tana qismi')
    photo = models.ImageField(upload_to='media/photo')
    links = models.CharField(max_length=100, verbose_name='link', blank=True)
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = "Userlar uchun"
        verbose_name_plural = "Userlar uchun"
    
 
    
class FoundDevice(models.Model):
    imei = models.ForeignKey(DeviceImei, on_delete=models.CASCADE)
    active_started = models.DateField(verbose_name="Birinchi faollik")
    active_finished = models.DateField(verbose_name="So'ngi faollik")
    operator = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=13,validators=[validate_phone_number],verbose_name="Telefon raqami")
    is_viewed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Topilgan qurilma"
        verbose_name_plural = "Topilgan qurilmalar"

    def __str__(self):
        return f"{self.imei.device.device_name} - {self.phone_number}"