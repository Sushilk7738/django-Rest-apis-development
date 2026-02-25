from django.shortcuts import render
from players.models import Players
from .serializers import PlayerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#* for class based
from rest_framework.views import APIView
from django.http import Http404



# @api_view(['GET', 'POST'])
# def players(request):
#     player = Players.objects.all()
#     serializer = PlayerSerializer(player, many = True)

#     if request.method == 'GET':
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     elif request.method == 'POST':
#         serializer = PlayerSerializer(data = request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
# @api_view(['GET', 'PUT', 'DELETE'])
# def player_details(request, pk):
#     try:
#         player = Players.objects.get(pk = pk)
#     except Players.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = PlayerSerializer(player)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     elif request.method == 'PUT':
#         serializer = PlayerSerializer(player, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         player.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



class Player(APIView):
    def get(self, request):
        player = Players.objects.all()
        serializer = PlayerSerializer(player, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PlayerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlayerDetails(APIView):
    def get_object(self, pk):
        try:
            return Players.objects.get(pk=pk)
        except Players.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        player = self.get_object(pk)
        serializer = PlayerSerializer(player)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        player = self.get_object(pk)
        serializer = PlayerSerializer(player, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        player = self.get_object(pk)
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


        