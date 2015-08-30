import posixpath

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
    print "league!!!"
    t = loader.get_template('statistics/league.html')
    l = League.objects.get(id=league)
    games = Game.objects.filter(league=l)
    c = RequestContext(request, {
        'league': l,
        'games': games,
        'source': resturl(request, league)
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

def team(request, league):
    l = League.objects.get(id=league)
    t = loader.get_template('statistics/team.html')
    c = RequestContext(request, {
        'league': l,
        'source': resturl(request, league)
    })
    return HttpResponse(t.render(c))

def game(request, league):
    l = League.objects.get(id=league)
    t = loader.get_template('statistics/game.html')
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
