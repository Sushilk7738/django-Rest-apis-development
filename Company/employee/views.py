from django.shortcuts import render
from .models import Company, Employee
from .serializers import EmpSerializer, CompanySerializer
from rest_framework.views import APIView
from rest_framework import generics

class CompanyView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpSerializer
