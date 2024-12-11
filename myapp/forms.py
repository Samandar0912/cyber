import re
from django import forms
from .models import *
from django.forms import inlineformset_factory
from .validators import  validate_file_size, validate_file_extension
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm




class AccountForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Parol'
        }),
        label="Parol",
        required=False
    )

    class Meta:
        model = Account
        fields = ['username', 'first_name', 'last_name', 'phone_number', 'password','lavel']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Foydalanuvchi nomi'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ism'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Familiya'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telefon raqami (+998XXXXXXXXX)'
            }),
            'lavel': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Lavozimi'
            }),
        }
        labels = {
            'username': 'Foydalanuvchi nomi',
            'first_name': 'Ism',
            'last_name': 'Familiya',
            'phone_number': 'Telefon raqami',
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        password = self.cleaned_data.get("password")

        if password:
            instance.set_password(password)
        if commit:
            instance.save()
        return instance


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Viloyat nomi'}),
        }

class DeviceTypeForm(forms.ModelForm):
    class Meta:
        model = DeviceType
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Qurilma turi'}),
        }

class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ['categoryRegion', 'title']
        widgets = {
            'categoryRegion': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tuman nomi'}),
        }



class DeviceImeiForm(forms.ModelForm):        
    class Meta:
        model = DeviceImei
        fields = ['imei']

 
DeviceIMEIFormSet = inlineformset_factory(
    UserDevice,
    DeviceImei,
    form=DeviceImeiForm,
    extra=1,
    can_delete=True
)


class UserDeviseForm(forms.ModelForm):    
    imei_formset = DeviceIMEIFormSet()  # Formsetni ta'riflash
    
    class Meta:
        model = UserDevice
        fields = ['name', 'categoryRegion', 'categoryDistrict', 'device_type', 'device_name', 'data', 'phone_number', 'file']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ism'}),
            'categoryRegion': forms.Select(attrs={'class': 'form-control'}),
            'categoryDistrict': forms.Select(attrs={'class': 'form-control'}),
            'device_type': forms.Select(attrs={'class': 'form-control'}),
            'device_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Qurilma nomi'}),
            'data': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "+998..."}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        validate_phone_number(phone_number)  # Call custom phone number validator
        return phone_number

    def clean_file(self):
        file = self.cleaned_data.get('file')
        validate_file_size(file)  # Custom validator for file size
        validate_file_extension(file)  # Custom validator for file extension
        return file

    def save(self, commit=True):
        device = super().save(commit=False)
        print("salom")
        
        imei_formset = self.imei_formset
        if imei_formset.is_valid():
            for form in imei_formset:
                if form.cleaned_data.get('imei'):
                    imei = form.cleaned_data['imei']
                    DeviceImei.objects.create(device=device, imei=imei)
        
        if commit:
            device.save()  
        return device

   
    






# Viloyat formasi
class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Viloyat nomini kiriting'}),
        }
        labels = {
            'title': 'Viloyat',
        }


# Qurilma turi formasi
class DeviceTypeForm(forms.ModelForm):
    class Meta:
        model = DeviceType
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Qurilma turini kiriting'}),
        }
        labels = {
            'title': 'Qurilma turi',
        }


# Tuman formasi
class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ['categoryRegion', 'title']
        widgets = {
            'categoryRegion': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tuman nomini kiriting'}),
        }
        labels = {
            'categoryRegion': 'Viloyat',
            'title': 'Tuman nomi',
        }
        
        


class UsersNoteForm(forms.ModelForm):
    class Meta:
        model = UsersNote
        fields = ['title', 'body', 'photo','links']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sarlavha kiriting'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Matnni kiriting', 'rows': 5}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'links': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Link kiriting'}),
        }
        
