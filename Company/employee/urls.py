from django.urls import path
from . import views
urlpatterns = [
    path('emp/', views.EmployeeView.as_view()),
    path('cmp/', views.CompanyView.as_view()),
]
