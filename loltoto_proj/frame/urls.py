from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show/', views.show, name='show_tournaments'),
    path('create/', views.create, name='create_tournament'),
    
    #tournament
    path('tournament/', views.tournament_produce, name='tournament_produce'),
    path('participate_tournament/', views.tournament_participation, name='tournament_participation'),
    path('confirm_tournament/', views.tournament_confirmation, name='tournament_confirmation'),

    #team
    path('create_team/', views.create_team, name = 'create_team'),
    path('regist_summoner/', views.regist_summoner, name='regist_summoner'),


    # /0x2DA/2/
    path('tournament/<str:producer>/<int:tournamentID>', views.tournament_detail, name='tournament_detail'),
    path('producers/', views.producer_list, name='producer_list')
]