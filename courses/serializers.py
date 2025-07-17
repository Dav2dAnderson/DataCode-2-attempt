from rest_framework import serializers

from .models import Course, Modules, Lesson, LessonFile


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'slug', 'price', 'image']


class CourseDetailSerializer(serializers.ModelSerializer):
    teacher = serializers.CharField(source='teacher.username', read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'name', 'slug', 'description', 'price', 'created_at', 'image', 'teacher_id', 'teacher']

    
class ModuleSerializer(serializers.ModelSerializer):
    course = serializers.CharField(source='course.name', read_only=True)
    class Meta:
        model = Modules
        fields = ['name', 'course', 'file']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'module']


class LessonDetailSerializer(serializers.ModelSerializer):
    lesson_files = serializers.SerializerMethodField()
    class Meta:
        model = Lesson
        fields = ['title', 'description', 'module', 'is_active', 'created_at', 'updated_at', 'lesson_files']

    def get_lesson_files(self, obj):
        files = obj.lesson_files.all()
        return LessonFilesSerializer(files, many=True).data


class LessonFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonFile
        fields = ['id', 'file', 'lesson']