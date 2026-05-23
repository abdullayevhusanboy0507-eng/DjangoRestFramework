from django.urls import path

from .views import CourseAPIView, StudentAPIView

urlpatterns = [
    path('course/',CourseAPIView.as_view()),
    path('course/<int:pk>/',CourseAPIView.as_view()),
    path('student/',StudentAPIView.as_view()),
    path('student/<int:pk>/',StudentAPIView.as_view()),
]