# from django.shortcuts import render
# from django.http import JsonResponse
from employee.models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404




# def emp_info(request):
#     employee = Employee.objects.all()

#     #* Handling manual serializer
#     employee_list = list(employee.values())
#     return JsonResponse(employee_list, safe=False)


#* By using serializer:-

# @api_view(['GET', 'POST'])
# def emp_info(request):
#     if request.method == "GET":
#         employee = Employee.objects.all()
#         serializer = EmployeeSerializer(employee, many =True)

#         return Response(serializer.data,status=status.HTTP_200_OK)

#     elif request.method == "POST":
#         serializer = EmployeeSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         print(serializer.errors)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET', 'PUT', 'DELETE'])
# def emp_detail_view(request, pk):
#     try:
#         emp = Employee.objects.get(pk = pk)
#     except Employee.DoesNotExist:
#         return Response(status= status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = EmployeeSerializer(emp)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'PUT':
#         serializer = EmployeeSerializer(emp, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     elif request.method == 'DELETE':
#         emp.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

    
#* class based view

class EmpInfo(APIView):
    def get(self,request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        raise Response(status=status.HTTP_400_BAD_REQUEST)


class EmpDetails(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        employees = self.get_object(pk)
        serializer = EmployeeSerializer(employees)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        employees = self.get_object(pk)
        serializer = EmployeeSerializer(employees, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employees = self.get_object(pk)
        employees.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)