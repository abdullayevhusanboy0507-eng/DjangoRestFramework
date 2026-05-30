from rest_framework import serializers


class CourseSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length = 255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    
    
class StudentSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length = 255)
    first_name = serializers.CharField(max_length = 255)
    year = serializers.DateTimeField()

    