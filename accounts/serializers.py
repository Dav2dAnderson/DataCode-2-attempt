from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework import serializers
from rest_framework.authentication import get_user_model

from django.contrib.auth import authenticate

from .models import CustomRole, Notification

# from courses.models import Course
from courses.serializers import CourseSerializer

""" dj-rest-auth classes """
from dj_rest_auth.serializers import UserDetailsSerializer, PasswordChangeSerializer

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
""" """



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


class UserNotificationsSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer(read_only=True)
    class Meta:
        model = Notification
        fields = ['id', 'user', 'content', 'date']

