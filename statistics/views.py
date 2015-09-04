import posixpath
from datetime import datetime

from django.template import RequestContext, loader
from django.http import HttpResponse
#from torpedo_main.menu import get_menu, RootMenu, MenuItem
from statistics.models import League, Team, Game, Player, Goal, Penalty
from django.utils.translation import ugettext as _
from django.http.response import HttpResponseRedirect


from rest_framework import viewsets
from statistics.serializers import LeagueSerializer, TeamSerializer,\
GameSerializer, PlayerSerializer, GoalSerializer, PenaltySerializer


# def rooturl(lid):
#     return '/statistics/%s/' % lid

def resturl(request, lid):
    restpath = posixpath.abspath(posixpath.join(request.path, '../rest'))
    return '%s?league=%s' % (restpath, lid)

def default(request):
    print "default!!"
    t = loader.get_template('statistics/main.html')
    c = RequestContext(request, {
        'leagues': League.objects.all(),
    })
    return HttpResponse(t.render(c))

def league(request, league):
    l = League.objects.get(id=league)
    if request.method == 'POST':
        date = datetime.strptime(request.POST.get('date'), '%d-%m-%Y %H:%M')
        home = request.POST.get('home')
        guest = request.POST.get('guest')
        home_team, hc = Team.objects.get_or_create(name=home, league=l)
        guest_team, gc = Team.objects.get_or_create(name=guest, league=l)
        game = Game.objects.create(
            date=date,
            home=home_team,
            guest=guest_team,
            league=l)
        if hc:
            home_team.save()
        if gc:
            guest_team.save()
        game.save()

    t = loader.get_template('statistics/league.html')
    games = Game.objects.filter(league=l)
    teams = Team.objects.filter(league=l)
    c = RequestContext(request, {
        'league': l,
        'games': games,
        'teams': teams,
        'source': resturl(request, league)
    })
    return HttpResponse(t.render(c))

def team(request, league, team):
    l = League.objects.get(id=league)
    team = Team.objects.get(id=team)
    if request.method == 'POST':
        number = request.POST.get('number')
        name = request.POST.get('name')
        print "Saving a new player"
        player = Player.objects.create(
            number=number,
            name=name,
            team=team,
            league=l)
        player.save()

    teamplayers = Player.objects.filter(team=team, league=league).order_by('number')


    t = loader.get_template('statistics/team.html')
    c = RequestContext(request, {
        'league': l,
        'team': team,
        'players': teamplayers,
        'source': resturl(request, league)
    })
    return HttpResponse(t.render(c))

def game(request, league, game):
    l = League.objects.get(id=league)
    game = Game.objects.get(id=game)
    if request.method == 'POST':
        print request.POST
        time = '00:%s' % request.POST['time']
        if request.POST.get('type') == 'goal':
            if request.POST['team'] == 'home':
                team = game.home
            else:
                team = game.guest
            player = Player.objects.get(id=request.POST['player'])
            if request.POST['assisting'] != 'N/A':
                assisting = Player.objects.get(id=request.POST['assisting'])
            else:
                assisting = None
            note = request.POST['note']
            Goal.objects.create(
                time=time,
                game=game,
                team=team,
                player=player,
                assisting=assisting,
                note=note,
                league=l
            )
        elif request.POST.get('type') == 'penalty':
            if request.POST['team'] == 'home':
                team = game.home
            else:
                team = game.guest
            player = Player.objects.get(id=request.POST['player'])
            reason = request.POST['reason']
            duration = request.POST['duration']
            Penalty.objects.create(
                time=time,
                game=game,
                team=team,
                player=player,
                length=duration,
                reason=reason,
                league=l
            )

    goals = Goal.objects.filter(game=game).order_by('-time')
    penalties = Penalty.objects.filter(game=game).order_by('-time')
    # Create events
    events = []
    for goal in goals:
        event = { "type": "goal",
                  "id": goal.id,
                  "time": goal.time,
                  "game": goal.game,
                  "team": goal.team,
                  "player": goal.player,
                  "assisting": goal.assisting,
                  "note": goal.note}
        events.append(event)
    for penalty in penalties:
        event = { "type": "penalty",
                  "id": penalty.id,
                  "time": penalty.time,
                  "game": penalty.game,
                  "team": penalty.team,
                  "player": penalty.player,
                  "duration": penalty.length,
                  "reason": penalty.reason}

        events.append(event)
    events.sort(key=lambda e: e['time'], reverse=True)
    t = loader.get_template('statistics/game.html')
    c = RequestContext(request, {
        'league': l,
        'game': game,
        'events': events,
        'goals': goals,
        'source': resturl(request, league)
    })
    return HttpResponse(t.render(c))

def games(request, league):
    l = League.objects.get(id=league)
    t = loader.get_template('statistics/games.html')
    c = RequestContext(request, {
        'league': l,
        'source': resturl(request, league)
    })
    return HttpResponse(t.render(c))

def teams(request, league):
    l = League.objects.get(id=league)
    t = loader.get_template('statistics/teams.html')
    c = RequestContext(request, {
        'league': l,
        'source': resturl(request, league)
    })
    return HttpResponse(t.render(c))

def players_dlg(request, league):
    l = League.objects.get(id=league)
    t = loader.get_template('statistics/players_dlg.html')
    players = Player.objects.all()
    c = RequestContext(request, {
        'league': l,
        'source': resturl(request, league),
        'players': players
    })
    return HttpResponse(t.render(c))


def statistics(request, league):
    print "statistics!!!"
    t = loader.get_template('statistics/main.html')
    l = League.objects.get(id=league)
    c = RequestContext(request, {
        'league': l,
        'leagues': League.objects.all(),
        'source': resturl(request, league)
    })
    return HttpResponse(t.render(c))

def players(request, league):
    l = League.objects.get(id=league)
    t = loader.get_template('statistics/players.html')
    c = RequestContext(request, {
        'league': l,
        'source': resturl(request, league)
    })
    return HttpResponse(t.render(c))




class LeagueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = League.objects.all().order_by('-from_date')
    serializer_class = LeagueSerializer

class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer

class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Game.objects.all().order_by('date')
    serializer_class = GameSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Player.objects.all().order_by('name')
    serializer_class = PlayerSerializer

class GoalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Goal.objects.all().order_by('time')
    serializer_class = GoalSerializer

class PenaltyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Penalty.objects.all().order_by('time')
    serializer_class = PenaltySerializer
