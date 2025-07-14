from django.contrib import admin

from .models import CustomRole, CustomUser, Notification, Testemonials, BlacklistedAccessToken

# Register your models here.


@admin.register(CustomRole)
class CustomRoleAdmin(admin.ModelAdmin):
    list_display = ['role']


@admin.register(CustomUser)
class CustomRoleAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_number', 'role']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user']


@admin.register(Testemonials)
class TestemonialsAdmin(admin.ModelAdmin):
    list_display = ['user']


@admin.register(BlacklistedAccessToken)
class BlackListedAdmin(admin.ModelAdmin):
    list_display = ['token']