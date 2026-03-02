from rest_framework import serializers
from .models import Employee, Company

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class CompanySerializer(serializers.ModelSerializer):
    employees = EmpSerializer(many =True, read_only = True)
    class Meta:
        model = Company
        fields = "__all__"