from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Doctors



def doc_info(request):
    doctors = Doctors.objects.all()
    doctors.list = list(doctors.values())
    return JsonResponse(doctors.list, safe=False)
    # return HttpResponse('<h2>We are the best doctors</h2>')
    