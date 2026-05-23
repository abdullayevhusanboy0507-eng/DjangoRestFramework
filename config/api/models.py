from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    def __str__(self):
        return f'{self.name}--{self.price}'
    
    
class Student(models.Model):
    name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    year = models.DateTimeField()
    bio = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    
    
    def __str__(self):
        return self.name
    
    
