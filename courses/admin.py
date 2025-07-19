from django.contrib import admin

from .models import Course, Lesson, LessonFile, Modules
# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'teacher', 'created_at']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']


@admin.register(LessonFile)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['file', 'lesson']


@admin.register(Modules)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['course', 'name', 'created_at', 'updated_at']

