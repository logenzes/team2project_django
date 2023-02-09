from django.urls import path
from games import views

app_name = "games"

urlpatterns = [
    path('', views.game_list, name="game_list"),
    path(r'game/<int:gameid>', views.game_view, name="game_view")
]