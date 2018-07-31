from django.db import models

# Create your models here.

class Producer(models.Model):
    producer_addr = models.CharField(primary_key = True, max_length=40)
    nonce = models.IntegerField(default=0)

class Award(models.Model):
    participants = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    multi = models.IntegerField(default=0)
    

class Tournament(models.Model):
    tournament_code = models.CharField(max_length=200, primary_key = True)
    tournament_name = models.CharField(max_length=200, default = '')
    producer_addr = models.ForeignKey(Producer, on_delete=models.CASCADE)
    producer_name = models.CharField(max_length=100, default='')
    nonce = models.IntegerField(default=0)

    max_teams = models.IntegerField(default=0)
    cur_teams = models.IntegerField(default=0)

    magnification = models.FloatField(default=0)
    initial_reward = models.FloatField(default=0)
    total_prize = models.FloatField(default=0)
    date = models.DateTimeField(default=0)
    place = models.CharField(default='')

    teams = models.CharField(max_length=640, default='')

class Team(models.Model):
    team_name = models.CharField(primary_key = True, max_length=20)
    account = models.CharField(max_length=40)
    
class Team_Tournament(models.Model):
    team_key = models.ForeignKey(Team, on_delete=models.CASCADE)
    tournament_key = models.ForeignKey(Tournament, on_delete=models.CASCADE)

class Summoner(models.Model):
    summoner_name = models.CharField(primary_key = True, max_length = 20)
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING)

class Match(models.Model):
    tournament_code = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    match_ID = models.IntegerField(default=0, primary_key=True)
    betting_end = models.DateTimeField('')
    team1 = models.CharField(default = "", max_length=20)
    team2 = models.CharField(default = '', max_length=20)