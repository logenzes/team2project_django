from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from games.models import Games, Score
from datetime import datetime
import json

class MypageView(TemplateView):
    template_name = 'mypage.html'

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, username = request.user)
        scores = Score.objects.filter(user_id = user.id)
        mypages = {}
        for score in scores:
            game = Games.all_games.get(id=score.games_id.id)
            print(score.insert_date)
            print(datetime.strftime(score.insert_date, "%Y-%m-%d"))
            datetime_key = datetime.strftime(score.insert_date, "%Y-%m-%d")
            if mypages.get(datetime_key) is None:
                mypages[datetime_key] = []
            mypages[datetime_key].append({'scores' : json.loads(score.score_data), 'game':game})

        print(mypages)
        context = {'mypages' : mypages}
        return render(request, self.template_name, context)

def MyapageRanking(request):
    user = get_object_or_404(User, username = request.user)
    print(user.id)
    scores = Score.objects.all()
    games = Games.show.all()
    rankingList = {}
    myList = {}
    for score in scores:
        if rankingList.get(score.games_id.id) is None:
            rankingList[score.games_id.id] = []
            myList[score.games_id.id] = []
        # print(score.score_data)
        rankingList[score.games_id.id].append(score)

    # 순위 변경
    for key, rank in rankingList.items():
        data = sorted(rank, key= lambda x : -x.total)
        # 순위 만들기
        i = 0
        for score in data:
            i += 1
            score.ranking =i

        rankingList[key] = data

        userlist=list(filter(lambda x: x.user_id==request.user, data))
        userlist = sorted(userlist, key=lambda x : x.ranking)
        myList[key] = userlist

    context = {'games': games, 'ranking':rankingList, 'myrank':myList}

    return render(request, "ranking.html", context)

# class RankingView(TemplateView):
#     template_name = 'ranking.html'
#
#     def get(self, request, *args, **kwargs):
#         user = get_object_or_404(User, username = )