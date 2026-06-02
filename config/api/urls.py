from django.urls import path

from .views import CourseAPIView, CourseRetreveAPIView, StudentAPIView, StudentRetreveAPIView

urlpatterns = [
    path('course/',CourseAPIView.as_view()),
    path('course/<int:course_id>/',CourseRetreveAPIView.as_view()),
    
    path('student/',StudentAPIView.as_view()),
    path('student/course/<int:student_id>/',StudentRetreveAPIView.as_view()),
    
    path('student/<int:student_id>/',StudentRetreveAPIView.as_view()),
]