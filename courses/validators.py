from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

phone_validator = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="Telefon raqami noto'g'ri kiritildi."
)


def validate_file_extension(value):
    valid_extensions = ['.pdf', '.jpg', '.jpeg', '.png', 'mp4', '.mkv', '.doc', 'docx']
    if not any(value.name.lower().endswith(ext) for ext in valid_extensions):
        raise ValidationError("Faqat DOC, DOCX, PDF, JPG, JPEG, PNG, MP4 va MKV formatidagi fayllar qabul qilinadi.")