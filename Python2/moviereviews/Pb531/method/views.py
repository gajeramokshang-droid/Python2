from django.shortcuts import render,redirect,get_object_or_404
from .models import Course
from .serializers import CourseSerializer
from rest_framework import viewsets

class CourseViewset(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

