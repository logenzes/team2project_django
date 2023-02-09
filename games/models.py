from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

import json

class ShowGames(models.Manager):
    def get_queryset(self):
        qs = super(ShowGames, self).get_queryset()
        return qs.filter(is_show = True)
class AllGames(models.Manager):
    def get_gueryset(self):
        qs = super(AllGames, self).get_queryset()
        return  qs

class Games(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField('타이틀', max_length=100)
    description = models.TextField('설명')
    game_html = models.CharField('게임html',max_length=100)
    img_src = models.CharField('이미지src', max_length=100, default='')
    is_show = models.BooleanField('show', default=True)
    insert_date = models.DateTimeField('insert date')
    update_date = models.DateTimeField('update date')

    show = ShowGames()
    all_games = AllGames()

    class Mete:
        verbose_name ="Game"
        verbose_name_plural = "Games"
        ordering = ['-insert_date']


    def save(self, *args, **kwargs):
        if not self.id:
            self.insert_date = now()
        self.update_date = now()

        super(Games, self).save(*args, **kwargs)

class Score(models.Model):
    id = models.BigAutoField(help_text = "score id", primary_key=True)
    score_data = models.CharField("점수정보", max_length=100)
    insert_date = models.DateTimeField('insert date', default=timezone.localtime())
    total = models.FloatField("총점", default=0)

    user_id = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, db_column="user_id")
    games_id = models.ForeignKey(Games, related_name="game", on_delete=models.CASCADE, db_column="games_id")

    @property
    def total(self):
        score_total = 0
        score_info = json.loads(self.score_data)

        if self.games_id.id == 1 or self.games_id.id == 4 or self.games_id.id == 5:
            score_total = score_info['score']
        elif self.games_id.id == 2 :
            stars = score_info['score']*100
            moves = score_info['moves']*score_info['score']
            score_total = stars + moves
        elif self.games_id.id == 3 :
            score = score_info['score']
            lives = score_info['lives']*10
            score_total = score + lives

        return score_total

    class Meta:
        verbose_name = "Score"
        verbose_name_plural = "Scores"
        ordering = ['-insert_date']

    def save(self, *args, **kwargs):
        self.insert_date = timezone.localtime()
        print(self.insert_date)
        super(Score, self).save(*args, **kwargs)  # 마지막에 부모의 함수를 호출


