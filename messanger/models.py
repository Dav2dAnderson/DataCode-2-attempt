from django.db import models
from django.utils.text import slugify

from accounts.models import CustomUser

# Create your models here.


class Chat(models.Model):
    chat_title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=55, null=True, blank=True)
    participants = models.ManyToManyField(CustomUser, related_name='participants')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.chat_title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.chat_title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Chat"
        verbose_name_plural = "Chats"


class Messages(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
