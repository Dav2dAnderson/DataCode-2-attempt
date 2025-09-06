from django.urls import path, include

from rest_framework_simplejwt.views import TokenRefreshView

from .views import MyTokenObtainPairView, UserRegistrationView, UserNotifications


urlpatterns = [
    # JWT Auth
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Own views associated with user actions
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('notifications/', UserNotifications.as_view(), name='notifications-list'),
    path('notifications/<int:pk>/', UserNotifications.as_view(), name='notification-detail'),
]

