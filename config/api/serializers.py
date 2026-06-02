from rest_framework import serializers

from .models import Course, Student


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
    
    
class StudentSerializers(serializers.ModelSerializer):
    course_write = serializers.ChoiceField(
        choices=Course.objects.all(),
        write_only=True)
    
    class Meta:
        model = Student
        fields = ['id','name','first_name','year','bio','course_write']
        depth = 1
        
    def create(self, validated_data):
        course_write = validated_data.pop('course_write')
        student = Student.objects.create(course=course_write,**validated_data)
        student.save()
        return student
    
    def update(self, instance, validated_data):
        instance.course = validated_data.pop('course_write') or instance.course
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
            
    