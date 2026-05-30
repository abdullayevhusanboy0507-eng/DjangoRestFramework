from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404

from .models import Course, Student
from .serializers import CourseSerializers, StudentSerializers

class CourseAPIView(APIView):
    def get(self, request: Request, pk: int = None):
        if not pk:
            coursies = Course.objects.all()
            return Response(CourseSerializers(coursies, many = True).data)
        else:
            course = get_object_or_404(Course, pk=pk)
            return Response(CourseSerializers(course).data)
    
    
    def post(self, request: Request, pk = None):
        if pk:
            return Response({"message": "Method POST not allowed"}, status=405)

        serializer = CourseSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        course = Course.objects.create(**serializer.validated_data)
        return Response(CourseSerializers(course).data)
    
    
    def put(self, request: Request, pk: int = None):
        if pk:
            course = get_object_or_404(Course, pk=pk)
            serializer = CourseSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            course.name = serializer.validated_data.get("name", course.name)
            course.price = serializer.validated_data.get("price", course.price)
            course.save()
            
            return Response(CourseSerializers(course).data)
        else:
            return Response({"message": "Method PUT not allowed"}, status=405)
        
        
    def delete(self, request: Request, pk: int = None):
        if not pk:
            return Response({"message":"Method DELETE not allowed"}, status=405)
        else:
            course = get_object_or_404(Course, pk=pk)
            course.delete()
            return Response({"message":"Course deleted successful"}, status=204)
        
        
class StudentAPIView(APIView):
    def get(self, request: Request, pk: int=None):
        if not pk:
            students = Student.objects.all()
            return Response(StudentSerializers(students, many=True).data)
        else:
            student = get_object_or_404(Student, pk=pk)
            return Response(StudentSerializers(student).data)
     
        
    def post(self,request: Request, pk=None):
        if pk:
            return Response({"message": "Method POST not allowed"}, status=405)
        
        serializer = StudentSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = Student.objects.create(**serializer.validated_data)
        return Response(StudentSerializers(student).data)
    
    
    def put(self, request: Request, pk: int = None):
        if pk:
            student = get_object_or_404(Student, pk=pk)
            serializer = StudentSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            student.name = serializer.validated_data.get("name", student.name)
            student.first_name = serializer.validated_data.get("first_name", student.first_name)
            student.year = serializer.validated_data.get("year", student.year)
            student.bio = serializer.validated_data.get("bio", student.bio)
            student.save()
            
            return Response(StudentSerializers(student).data)
        else:
            return Response({"message": "Method PUT not allowed"}, status=405)
        
        
    def delete(self, request: Request, pk: int = None):
        if not pk:
            return Response({"message":"Method DELETE not allowed"}, status=405)
        else:
            student = get_object_or_404(Student, pk=pk)
            student.delete()
            return Response({"message":"Course deleted successful"}, status=204)
        