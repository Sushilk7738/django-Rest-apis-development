from django.shortcuts import render
from Doctors.models import Doctors
from .serializers import DoctorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from django.http import Http404


# @api_view(['GET', 'POST'])
# def doc_view(request):
#     doctors = Doctors.objects.all()
#     serializer = DoctorSerializer(doctors, many = True)

#     if request.method == "GET":
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'POST':
#         serializer = DoctorSerializer(data = request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# @api_view(['GET', 'PUT', 'DELETE'])
# def doc_detail_view(request, pk):
#     try:
#         doctors = Doctors.objects.get(pk=pk)
#     except Doctors.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = DoctorSerializer(doctors)
#         return Response(serializer.data, status= status.HTTP_200_OK)
    
#     elif request.method == 'PUT':
#         serializer = DoctorSerializer(doctors, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         doctors.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



class DocView(APIView):
    def get(self, request):
        doctors = Doctors.objects.all()
        serializer = DoctorSerializer(doctors, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DoctorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DocDetails(APIView):
    def get_object(self, pk):
        try:
            return Doctors.objects.get(pk=pk)
        except Doctors.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        doctors = self.get_object(pk)
        serializer = DoctorSerializer(doctors)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        doctors = self.get_object(pk)
        serializer = DoctorSerializer(doctors, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        doctors = self.get_object(pk)
        doctors.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
