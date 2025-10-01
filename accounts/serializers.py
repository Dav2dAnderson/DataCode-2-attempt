from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework import serializers
from rest_framework.authentication import get_user_model

from django.contrib.auth import authenticate

from .models import CustomRole, Notification

# from courses.models import Course
from courses.serializers import CourseSerializer

""" dj-rest-auth classes """
from dj_rest_auth.serializers import UserDetailsSerializer, PasswordChangeSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer

User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # token bilan birga keladigan ma'lumotlar
        token['username'] = user.username
        token['role'] = str(user.role)
        token['email'] = user.email
        token['phone_number'] = user.phone_number

        return token


""" dj-rest-auth override """

class CustomUserDetailSerializer(UserDetailsSerializer):
    courses = serializers.SerializerMethodField()

    class Meta(UserDetailsSerializer.Meta):
        model = User
        fields = UserDetailsSerializer.Meta.fields + (
            'pk',
            'username',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'biography',
            'city',
            'blog',
            'tg_account',
            'courses',
        )
        read_only_fields = ('email', )

    def get_courses(self, obj):
        courses = obj.courses.all()
        return CourseSerializer(courses, many=True).data


class CustomUserPasswordChangeSerializer(PasswordChangeSerializer):
    current_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Current password is incorrect")
        return value
    

class CustomUserRegistrationSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True, help_text="Enter your first name")
    last_name = serializers.CharField(required=True, help_text="Enter your last name")
    phone_number = serializers.CharField(required=True, max_length=15, help_text="Enter a valid phone number (max 15 digits)")

    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.phone_number = self.validated_data.get('phone_number', '')

        user.save(update_fields=['first_name', 'last_name', 'phone_number'])
        return user
""" """


class UserNotificationsSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer(read_only=True)
    class Meta:
        model = Notification
        fields = ['id', 'user', 'content', 'date']

