from django.urls import path
from . import views


urlpatterns = [
    
    # path('emp/', views.emp_info),
    # path('emp/<int:pk>', views.emp_detail_view),

    # class based urls
    
    path('emp/', views.EmpInfo.as_view()),
    path('emp/<int:pk>', views.EmpDetails.as_view()),
]
