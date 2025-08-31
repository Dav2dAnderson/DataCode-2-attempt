from django.contrib import admin

from .models import Chat, Messages
# Register your models here.

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['chat_title', 'slug', 'created_date']


@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ['user', 'chat', 'message', 'date']