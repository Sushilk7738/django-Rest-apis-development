from django.urls import path
from . import views


urlpatterns = [
    # path('', views.player_view),
    path('', views.player_list),
]
