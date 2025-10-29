from django.urls import path
from .views import StudentListCreateView

urlpatterns = [
path('api/students/',
StudentsListCreateView.as_view(),
name="student-list"),
]
