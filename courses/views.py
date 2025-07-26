from django.shortcuts import render
from django.http import FileResponse, Http404

from rest_framework import viewsets, status, permissions, views
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Course, Modules, Lesson, LessonFile
from .serializers import CourseSerializer, CourseDetailSerializer, ModuleSerializer, LessonSerializer, \
    LessonDetailSerializer, LessonFilesSerializer
from .permissions import IsRegisteredToCourse

import os

# Create your views here.


""" ViewSet for Courses """


class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'slug'

    @action(detail=True, methods=['POST'], url_path='join_to_course', url_name='join_to_course',
            permission_classes=[permissions.IsAuthenticated])
    def join_to_course(self, request, *args, **kwargs):
        user = self.request.user
        course = self.get_object()
        if course not in user.courses.all():
            user.courses.add(course)
            return Response({'message': "You have joined to the course."})
        return Response({'message': "You have already joined to the course."})

    @action(detail=True, methods=['POST'], url_name='leave_the_course', url_path='leave_the_course',
            permission_classes=[permissions.IsAuthenticated])
    def leave_the_course(self, request, *args, **kwargs):
        user = self.request.user
        course = self.get_object()
        if course in user.courses.all():
            user.courses.remove(course)
            return Response({'message': "You have left the course."})
        return Response({'message': "You have not joined to the course yet."})

    def get_serializer_class(self):
        if self.action == 'list':
            return CourseSerializer
        return CourseDetailSerializer


""" ViewSet for Modules """


class ModuleViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Modules.objects.all()
    serializer_class = ModuleSerializer
    lookup_field = 'slug'


""" ViewSet for Lessons """


class LessonViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Lesson.objects.all()
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return LessonSerializer
        return LessonDetailSerializer


""" ViewSet for files """


class LessonFilesViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = LessonFile.objects.all()
    serializer_class = LessonFilesSerializer


class DownloadLessonFileView(views.APIView):
    def get(self, request, pk):
        try:
            lesson_file = LessonFile.objects.get(pk=pk)
            file_path = lesson_file.file.path
            if os.path.exists(file_path):
                return FileResponse(open(file_path, 'rb'), as_attachment=True)
            raise Http404("File not found.")
        except LessonFile.DoesNotExist:
            raise Http404("File not found.")
