from django.db import models

# Create your models here.

class Producer(models.Model):
    producer_addr = models.CharField(primary_key = True, max_length=40)
    nonce = models.IntegerField(default=0)

class Tournament(models.Model):
    tournament_code = models.CharField(max_length=200, primary_key = True)
    producer_addr = models.ForeignKey(Producer, on_delete=models.CASCADE)
    nonce = models.IntegerField(default=0)

class Match(models.Model):
    tournament_code = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    match_ID = models.IntegerField(default=0, primary_key=True)
    betting_end = models.DateTimeField('')
