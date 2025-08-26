from django.urls import path, include

from rest_framework_simplejwt.views import TokenRefreshView

from .views import MyTokenObtainPairView, ProfileSettingsView, \
UserProfileView, UserRegistrationView, UserLogOutView, UserNotifications, UserResetPasswordView


urlpatterns = [
    # JWT Auth
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Own views associated with user actions
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('logout/', UserLogOutView.as_view(), name='logout'),
    path('settings/', ProfileSettingsView.as_view(), name='settings'),
    path('password-reset/', UserResetPasswordView.as_view(), name='password-reset'),
    path('notifications/', UserNotifications.as_view(), name='notifications-list'),
    path('notifications/<int:pk>/', UserNotifications.as_view(), name='notification-detail'),
    path('', UserProfileView.as_view(), name='profile')
]

