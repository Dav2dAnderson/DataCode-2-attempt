from rest_framework import serializers

from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'slug', 'price', 'image']


class CourseDetailSerializer(serializers.ModelSerializer):
    teacher = serializers.CharField(source='teacher.username', read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'name', 'slug', 'description', 'price', 'created_at', 'image', 'teacher_id', 'teacher']

    