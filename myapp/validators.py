from django.core.exceptions import ValidationError
import os, re

def validate_file_size(value):
    max_size_kb = 5120  # 5 MB
    if value.size > max_size_kb * 1024:
        raise ValidationError(f"Fayl hajmi {max_size_kb} KB dan oshmasligi kerak.")

def validate_file_extension(value):
    valid_extensions = ['.pdf']
    ext = os.path.splitext(value.name)[1].lower()  # Fayl kengaytmasini olish
    if ext not in valid_extensions:
        raise ValidationError(f"Faqat quyidagi kengaytmalar ruxsat etiladi: {', '.join(valid_extensions)}.")

def validate_imei(value):
    if len(str(value)) != 15 or not str(value).isdigit():
        raise ValidationError("IMEI raqami 15 ta raqamdan iborat bo‘lishi kerak.")

def validate_phone_number(value):
    phone_regex = re.compile(r'^\+998\d{9}$')
    if not phone_regex.match(value):
        raise ValidationError("Telefon raqami +998 bilan boshlanishi va 12 ta raqam bo‘lishi kerak.")
