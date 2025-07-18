from rest_framework import permissions

from .models import LessonFile, Lesson, Modules, Course


class IsRegisteredToCourse(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        lesson = obj.lesson
        course = lesson.module.course
        
        if request.method in permissions.SAFE_METHODS:
            return course.students.filter(id=user.id).exists()
        return False