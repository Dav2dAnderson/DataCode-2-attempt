from courses.models import Course
from .models import Notification, CustomUser

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save, sender=Course)
def after_course_created(sender, instance, created, **kwargs):
    if created:
        notifications = []
        notification = "Platforma'ga yangi kurs qo'shildi"
        for user_id in CustomUser.objects.all():
            notifications.append(
                Notification(user=user_id, content=notification)
            )
        Notification.objects.bulk_create(notifications)


@receiver(post_delete, sender=Course)
def after_course_deleted(sender, instance, **kwargs):
    notifications = []
    notification = "Platforma'dan kurs olib tashlandi"
    for user_id in CustomUser.objects.all():
        notifications.append(
            Notification(user=user_id, content=notification)
        )
    Notification.objects.bulk_create(notifications)
    
