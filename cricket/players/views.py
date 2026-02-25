from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Players

# def player_view(request):
    # players = {
    #     "name" : 'Kapil Dev',
    #     "role" : 'Indian Former Captain'
    # }
    
    # return HttpResponse('<h1"}>Welcome to the Indian Players Team</h1>')
    # return JsonResponse(players)


def player_list(request):
    player = Players.objects.all()
    player_list = list(player.values())
    return JsonResponse(player_list, safe=False)