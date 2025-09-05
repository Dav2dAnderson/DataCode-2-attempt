from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ChatView


router = DefaultRouter()

router.register("chats", ChatView, basename='chats')

urlpatterns = [
    path('', include(router.urls))
]