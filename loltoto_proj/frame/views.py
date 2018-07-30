from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core import serializers
from django.db.models.query import EmptyQuerySet
from django.contrib.sites.models import Site
from django.template import loader
from .models import *

def index(request):
    template = loader.get_template('frame/index.html')
    context = {
        'latest_question_list': 'www',
    }
    return HttpResponse(template.render(context, request)) 

def show(request):
    template = loader.get_template('frame/show.html')
    context = {
        'latest_question_list': 'www',
    }
    return HttpResponse(template.render(context, request)) 

def create(request):
    template = loader.get_template('frame/create.html')
    context = {
        'latest_question_list': 'www',
    }
    return HttpResponse(template.render(context, request)) 

# 토너먼트 리스트 출력. 기본 페이지.
def tournament_list(request):
    template = loader.get_template('frame/index.html')
    context = {
        'latest_question_list': 'www',
    }
    return HttpResponse(template.render(context, request))

    data = serializers.serialize('json', Tournament.objects.all())
    # return JSON file of tournament list.
    return HttpResponse(data)

# 토너먼트 생성
## 현재는 GET 방식으로 생성.
## get url: /produce?producer=PRODUCER_NAME
## 클라이언트와 연계해서 json으로 바꿔야 함
def tournament_produce(request):
    
    prod = request.GET['producer']
    prod_obj = Producer.objects.filter(producer_addr=prod)
    if prod_obj.count() == 0:
        # 새로 생성
        Producer.objects.create(producer_addr=prod)
    
    nonce = prod_obj.get(producer_addr=prod).nonce + 1
    prod_obj.update(nonce = nonce)
    tournament_code = str(request.build_absolute_uri(request.path)) + str(prod) +'/' + str(nonce)
    #tournament_code = str(request.current_app) + str(prod) +'/' + str(nonce)
    Tournament.objects.create(tournament_code = tournament_code,
                            producer_addr = Producer(prod))

    return HttpResponse("New tournament is created. <br> Your tournament code is: " + tournament_code)

# 토너먼트에 관련된 상세 정보를 출력
def tournament_detail(request, producer, tournamentID):
    obj = Tournament.objects.filter(producer_addr=producer, nonce=tournamentID)
    data = serializers.serialize('json', obj)
    # return JSON file of tournament list.
    return HttpResponse(str(data) + "<br><br>tournament_detail for <br> producer: %s <br> tournamentID: %s" % (producer, tournamentID))


# 저장된 생성자 리스트 출력.
def producer_list(request):
    data = serializers.serialize('json', Producer.objects.all())
    # return JSON file of tournament list.
    return HttpResponse(data)
