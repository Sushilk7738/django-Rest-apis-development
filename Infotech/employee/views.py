from django.shortcuts import render, HttpResponse
from django.http import JsonResponse


# def emp_view(request):
#     return HttpResponse('<h2>Welcome to the Infotech IT Company</h2>')

def emp_view(request):
    empInfo = {
        'id' : 6, 
        'name' : 'Sushil',
        'role' : 'Director'
    }
    
    return JsonResponse(empInfo)


