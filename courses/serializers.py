from rest_framework import serializers

from .models import Course, Modules, Lesson, LessonFile


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'slug', 'price', 'image']


class LessonDetailSerializer(serializers.ModelSerializer):
    lesson_files = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ['title', 'description', 'module', 'is_active', 'created_at', 'updated_at', 'lesson_files']

    def get_lesson_files(self, obj):
        user = self.context['request'].user
        course = obj.module.course

        if course.students.filter(id=user.id).exists():
            return LessonFilesSerializer(obj.lesson_files.all(), many=True).data
        return []


class LessonFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonFile
        fields = ['id', 'file', 'lesson']


class LessonSerializer(serializers.ModelSerializer):
    lesson_files = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ['title', 'slug', 'module', 'lesson_files']

    def get_lesson_files(self, obj):
        user = self.context['request'].user
        course = obj.module.course
        if course.students.filter(id=user.id).exists():
            return LessonFilesSerializer(obj.lesson_files.all(), many=True).data
        return []


class ModuleSerializer(serializers.ModelSerializer):
    course = serializers.CharField(source='course.name', read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Modules
        fields = ['name', 'course', 'file', 'lessons']


class CourseDetailSerializer(serializers.ModelSerializer):
    teacher = serializers.CharField(source='teacher.username', read_only=True)
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'slug', 'description', 'price', 'created_at', 'image', 'teacher_id', 'teacher',
                  'modules']
