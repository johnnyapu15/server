from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show/', views.show, name='show_tournaments'),
    path('create/', views.create, name='create_tournament'),
    path('tournament/', views.tournament_produce, name='tournament_produce'),
    # /0x2DA/2/
    path('tournament/<str:producer>/<int:tournamentID>', views.tournament_detail, name='tournament_detail'),
    path('producers/', views.producer_list, name='producer_list')
]