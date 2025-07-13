from django.urls import path, include

from rest_framework_simplejwt.views import TokenRefreshView

from .views import MyTokenObtainPairView, ProfileSettingsView, UserProfileView, UserRegistrationView, UserLogOutView


urlpatterns = [
    # JWT Auth
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Own views associated with user actions
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('logout/', UserLogOutView.as_view(), name='logout'),
    path('settings/', ProfileSettingsView.as_view(), name='settings'),
    path('', UserProfileView.as_view(), name='profile')
]

