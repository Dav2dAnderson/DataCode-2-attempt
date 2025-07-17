from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CourseViewSet, ModuleViewSet, LessonViewSet, LessonFilesViewSet, DownloadLessonFileView


router = DefaultRouter()
router.register('courses', CourseViewSet, basename='courses')
router.register('course_modules', ModuleViewSet, basename='course_modules')
router.register('lessons', LessonViewSet, basename='lessons')
router.register('lesson_files', LessonFilesViewSet, basename='lesson_files')


urlpatterns = [
    path('', include(router.urls)),
    path('lesson-file/download/<int:pk>/', DownloadLessonFileView.as_view(), name='lesson-file-download')
]

