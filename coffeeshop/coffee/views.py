from django.shortcuts import render
from .models import Coffee
from .serializers import CoffeeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class CoffeeList(APIView):
    def get(self, request):
        coffees = Coffee.objects.all()
        serializer = CoffeeSerializer(coffees, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CoffeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CoffeeDetail(APIView):
    def get(self, request, pk):
        coffee = Coffee.objects.get(id = pk)
        serializer = CoffeeSerializer(coffee)
        return Response(serializer.data)

    def put(self, request, pk):
        coffee = Coffee.objects.get(id = pk)
        serializer = CoffeeSerializer(coffee, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        coffee = Coffee.objects.get(id = pk)
        coffee.delete()
        return Response('{"message" : "Deleted Successfully"}')

