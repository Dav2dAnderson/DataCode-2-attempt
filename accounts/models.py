from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomRole(models.Model):
    role = models.CharField(max_length=50)
    
    def __str__(self):
        return self.role
    

class CustomUser(AbstractUser):
    picture = models.ImageField(upload_to='user_pictures/', null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    role = models.ForeignKey(CustomRole, on_delete=models.SET_NULL, null=True)
    courses = models.ManyToManyField("courses.Course", related_name='students', blank=True)
    tg_account = models.URLField(null=True, blank=True)
    blog = models.URLField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    muted = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ['username']
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Testemonials(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    written_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ['written_date']
        verbose_name = 'Testemonial'
        verbose_name_plural = 'Testemonials'


class BlacklistedAccessToken(models.Model):
    token = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token


class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'