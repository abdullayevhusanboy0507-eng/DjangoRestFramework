from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404

from .models import Course, Student


class CourseAPIView(APIView):
    def get(self, request: Request, pk: int = None):
        if not pk:
            coursies = Course.objects.all()
            course_list = []
            for course in coursies:
                course_list.append(
                    {
                        'id': course.pk,
                        'name': course.name,
                        'price':course.price
                    }
                )
            return Response(course_list)
        else:
            course = get_object_or_404(Course, pk=pk)
            return Response(model_to_dict(course))
        

class StudentAPIView(APIView):
    def get(self, request: Request, pk: int=None):
        if not pk:
            students = Student.objects.all()
            student_list = []
            for student in students:
                student_list.append(
                    {
                        'id': student.pk,
                        'name': student.name,
                        'first_name': student.first_name,
                        'year': student.year,
                        'bio': student.bio,
                        'course': student.course.id
                    }
                )
            return Response(student_list)
        else:
            student = get_object_or_404(Student, pk=pk)
            return Response(model_to_dict(student))