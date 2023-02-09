from django.urls import path
from mypage import views

app_name = "mypage"

urlpatterns = [
    path('', views.MypageView.as_view(), name="myGameScoreList"),
    path('ranking/', views.MyapageRanking, name="myapageRanking"),
]