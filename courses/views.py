from django.shortcuts import render

from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Course
from .serializers import CourseSerializer, CourseDetailSerializer
# Create your views here.


""" ViewSet for Courses """
class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'slug'

    @action(detail=True, methods=['POST'], url_path='join_to_course', url_name='join_to_course', permission_classes=[permissions.IsAuthenticated])
    def join_to_course(self, request, *args, **kwargs):
        user = self.request.user
        course = self.get_object()
        if course not in user.courses.all():
            user.courses.add(course)
            return Response({'message': "You have joined to the course."})
        return Response({'message': "You have already joined to the course."})
    
    @action(detail=True, methods=['POST'], url_name='leave_the_course', url_path='leave_the_course', permission_classes=[permissions.IsAuthenticated])
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
    pass


""" ViewSet for Lessons """
class LessonViewSet(viewsets.ModelViewSet):
    pass


""" ViewSet for files """
class LessonFilesViewSet(viewsets.ModelViewSet):
    pass


 

