from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Games, Score

# Create your views here.
def game_list(request):
    User = get_user_model()
    user = get_object_or_404(User, username=request.user)
    if request.user == user:
        games = Games.show.get_queryset()
        # .show.objects.get_queryset()
        game_list= []
        for game in games:
            game_list.append(game)

        context = {'games':game_list, 'user':{'username':request.user.username, 'userid':request.user.id}}


        return  render(request, 'game_list.html', context)
    auth.logout(request);
    return HttpResponseRedirect(reverse('users:login'))


def game_view(request, gameid):

    user = get_object_or_404(User, username=request.user)
    if request.user == user:
        game = get_object_or_404(Games, id=gameid)

        print(game)
        print(user)
        context = {'game':game, 'user':{'username':request.user.username, 'userid':request.user.id}}

        if request.method == "POST":
            user_id = request.user.id
            game_id = request.POST['game_id']
            score_value = request.POST['score_value']
            score = Score()
            score.score_data = score_value
            score.user_id = user
            score.games_id = game
            score.save()
            print(user_id,game_id,score_value)
        return  render(request, 'game.html', context)
    auth.logout(request);
    return HttpResponseRedirect(reverse('users:login'))