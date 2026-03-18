from django.urls import path
from . import views

urlpatterns = [
    path('', views.CoffeeList.as_view(), name='coffees'),
    path('coffee/<int:pk>', views.CoffeeDetail.as_view(), name='coffee_detail'),
    
]
