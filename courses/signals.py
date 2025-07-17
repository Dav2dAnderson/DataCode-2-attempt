from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Course

@receiver(post_save, sender=Course)
def after_course_created(sender, instance, created, **kwargs):
    if created:
        print("===================\nSalom. Platforma'ga yangi kurs qo'shildi.\n====================")


@receiver(post_delete, sender=Course)
def after_course_deleted(sender, instance, **kwargs):
    print("====================\nSalom. Platforma'dan kurs olib tashlandi.\n====================")