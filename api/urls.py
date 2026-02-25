from django.urls import path
from . import views

urlpatterns = [
    # function based
    # path('doc/', views.doc_view),
    # path('doc/<int:pk>/', views.doc_detail_view),

    
    # class based
    path('doc/', views.DocView.as_view()),
    path('doc/<int:pk>', views.DocDetails.as_view()),
]