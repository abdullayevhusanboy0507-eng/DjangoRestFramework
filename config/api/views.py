from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404

from .models import Course, Student
from .serializers import CourseSerializers, StudentSerializers

class CourseAPIView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers


class CourseRetreveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    lookup_field = 'pk'
    lookup_url_kwarg = 'course_id'


class StudentAPIView(ListCreateAPIView):

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        if course_id:
            return self.queryset.filter(course_id=course_id)
        return self.queryset.all()
    
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return StudentSerializers
        return StudentSerializers


class StudentRetreveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    lookup_field = 'pk'
    lookup_url_kwarg = 'student_id'
 
