from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework import serializers
from rest_framework.authentication import get_user_model

from .models import CustomRole

# from courses.models import Course
from courses.serializers import CourseSerializer

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


class ProfileSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'phone_number', 'email', 'biography', 'city', 'blog',
                  'tg_account']


class UserProfileSerializer(serializers.ModelSerializer):
    courses = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'phone_number', 'biography', 'courses']

    def get_courses(self, obj):
        courses = obj.courses.all()
        return CourseSerializer(courses, many=True).data


class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password', 'password_confirm']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError('Password do not match.')
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        role_instance = CustomRole.objects.get(role="student")
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            role=role_instance
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

# class UserCourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "courses.Course"
#         fields = ['id', 'name', 'teacher', 'is_active']
