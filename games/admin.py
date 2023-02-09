from django.contrib import admin
from .models import Games, Score

class GamesAdmin(admin.ModelAdmin):
    list_display = ('title', 'game_html', 'description', 'is_show', 'insert_date')
    # list_editable = ('title', 'game_html', 'description', 'is_show')
    list_filter = ('title', 'game_html')
    search_fields = ['title', 'game_html']
    readonly_fields = ('insert_date','update_date')

class ScoreAdming(admin.ModelAdmin):
    list_display = ('score_data', 'user_id', 'insert_date')


admin.site.register(Games, GamesAdmin)
admin.site.register(Score, ScoreAdming)
# Register your models here.
