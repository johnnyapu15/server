from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.core import serializers
from django.db.models.query import EmptyQuerySet
from django.contrib.sites.models import Site
from django.template import loader
from .models import *
from .pyt import eth
import re

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
    Tournament.objects.create(
        tournament_code = tournament_code,
        producer_addr = Producer(prod)
        # max_teams = par,
        # cur_teams = 0,
        # magnification = magni,
        # initial_reward = init,
        # teams = ''
                            )

    return HttpResponse("New tournament is created. <br> Your tournament code is: " + tournament_code)

def tournament_participation(request):
    # input:
    # 팀명
    # 토너먼트 코드

    #USE_FOR_TEST
    _tournament_code = request.GET['_tournament_code']
    _team_name = request.GET['_team_name']
    _account = request.GET['_account']


    #블록체인에 팀 계정이 참가비를 냈는 지 확인해야한다.
    if eth.isParticipated(_tournament_code, _account):
        obj = Tournament.objects.filter(tournament_code = _tournament_code)
        objs = obj.get(tournament_code = _tournament_code)
        obj.update(
            teams = objs.teams + "," + _team_name,
            cur_teams = objs.cur_teams + 1
        )
        Team_Tournament.objects.create(
            team_key = Team.objects.get(team_name = _team_name),
            tournament_key = objs
        )
                                
    else:
      # 아직 참가비를 내지 않았음.
      return Http404("아직 참가비 지불이 되지 않았습니다!")
    return HttpResponse("Good! 참가되었다.")

def tournament_confirmation(request):

    ####USE_FOR_TEST
    _tournament_code = request.GET['_tournament_code']
    _magni = request.GET['_magni']
    _init = request.GET['_init']
    _teams = request.GET['_teams']

    obj = Tournament.objects.filter(tournament_code = _tournament_code)
    obj.update(
        magnification = _magni,
        initial_reward = _init,
        teams = _teams
    )

    # 클라이언트에서 스마트 컨트랙트에 이 정보를 갱신하면서 진행해야 함.
    return 

# 팀 관리

def create_team(request):
    #input:
    # 계좌
    # 팀명
    # 올바른 계좌인 지 검사하는 것 추가해야 함.

    ####USE_FOR_TEST
    _account = request.GET['_account']
    _team_name = request.GET['_team_name']



    # p = re.compile('^[0-9A-Za-z]{40}$')
    # if p.match(_account):
       # 올바른 계좌
    if (str(_team_name).find(',') > 0):
        # 팀 이름에 , 불가
        raise Http404("팀 이름에 , 를 넣지 말아주세요.")
    Team.objects.create(
        team_name = _team_name,
        account = _account
    )
    
    # else:
    #     # 잘못된 계좌 길이
    #     raise Http404("계좌 주소가 잘못되었는데요...?")
    
    return HttpResponse("Good.")

def regist_summoner(request):
    # 추가하기전에 Riot API에서 검색한다? NONO
    # input:
    # 소환사아이디
    # 팀명
    # 팀 계좌

    ####USE_FOR_TEST
    _team_name = request.GET['_team_name']
    _account = request.GET['_account']
    _name = request.GET['_name']
    

    try:
        t_obj = Team.objects.get(pk = _team_name)
        
    except t_obj.DoesNotExist:
        raise Http404("Wrong Team Name...!")
    if _account == Team.objects.get(pk = _team_name).account:
        # 올바른 계좌일 경우
        Summoner.objects.create(
        summoner_name = _name,
        team = _Team(team_name = _team_name)
                            )
    
    return

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


# 상금 관련 계산 
def getMatch(_participants):
    return int(_participants / 2)

def getAwardList(_participants, _initial, _magni):
    awards = list()
    sum = 0
    p = _participants
    r = 1
    while (p > 1):
        li = list()
        for i in range(0, getMatch(p)):
            sum += _initial * r
            li.append(_initial * r)
        awards.append(li)
        p = p - getMatch(p)
        r *= _magni
    return awards, sum

def getMultiList(_participants):
    multi = list()
    p = _participants
    tmp = p - 1
    r = 1
    while (p > 1):
        for i in range(0, getMatch(p)):
            multi.append([r, tmp])
            tmp -= 1
        p = p - getMatch(p)
        r += 1
    return multi

def createRewardList(_participants):
    li = getMultiList(_participants)
    for i in li:
        Award(participants = _participants, rank = i[1], multi = i[0]).save()

