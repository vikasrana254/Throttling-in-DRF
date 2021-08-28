from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student 
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
# Create your views here.
class ModelViewStudent(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer 
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]