from django.urls import path
from . import views

urlpatterns = [
    #* function based
    # path('players/', views.players),
    # path('players/<int:pk>', views.player_details),

    #* Class based
    path('players/', views.Player.as_view()),
    path('players/<int:pk>', views.PlayerDetails.as_view()),
]
