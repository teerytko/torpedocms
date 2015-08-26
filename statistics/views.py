from django.template import RequestContext, loader
from django.http import HttpResponse
#from torpedo_main.menu import get_menu, RootMenu, MenuItem
from statistics.models import League, Team, Game, Player, Goal, Penalty
from django.utils.translation import ugettext as _
from django.http.response import HttpResponseRedirect

from rest_framework import viewsets
from statistics.serializers import LeagueSerializer, TeamSerializer,\
GameSerializer, PlayerSerializer, GoalSerializer, PenaltySerializer


# menu = get_menu()

# def rooturl(lid):
#     return '/statistics/%s/' % lid

# def resturl(lid):
#     return '/statistics/%s/rest/' % lid

# def get_breadcrums(request, league):
#     parts = request.path.strip('/').split('/')
#     breadcrumb = RootMenu()
#     breadcrumb.children['statistics'] = MenuItem(name=_('Statistics'), href='/statistics/%s' % league)
#     lobj = League.objects.get(id=league)
#     breadcrumb.children['league'] = MenuItem(name=lobj.name, href='/statistics/%s' % league)
#     for lobj in League.objects.all():
#         breadcrumb.children['league'].children[lobj.name] = MenuItem(name=lobj.name, href='/statistics/%s/' % lobj.id)
#     if len(parts) == 2: 
#         breadcrumb.children['next'] = MenuItem(name=_('next'), href='/statistics/%s' % league)
#         breadcrumb.children['next'].children['teams'] = MenuItem(name='Teams', href='/statistics/%s/teams' % league)
#         breadcrumb.children['next'].children['games'] = MenuItem(name='Games', href='/statistics/%s/games' % league)
#     elif parts[-1] == 'teams':
#         breadcrumb.children['teams'] = MenuItem(name=_('Teams'), href='/statistics/%s/teams' % league)
#         breadcrumb.children['teams'].children['games'] = MenuItem(name='Games', href='/statistics/%s/games' % league)
#     elif parts[-1] == 'games':
#         breadcrumb.children['games'] = MenuItem(name=_('Games'), href='/statistics/%s/games' % league)
#         breadcrumb.children['games'].children['teams'] = MenuItem(name='Teams', href='/statistics/%s/teams' % league)
#     elif parts[-1] == 'team':
#         breadcrumb.children['teams'] = MenuItem(name=_('Teams'), href='/statistics/%s/teams' % league)
#         breadcrumb.children['teams'].children['games'] = MenuItem(name='Games', href='/statistics/%s/games' % league)
#         breadcrumb.children['team'] = MenuItem(name=_('Team'), href='/statistics/%s/team' % league)
#     elif parts[-1] == 'game':
#         breadcrumb.children['games'] = MenuItem(name=_('Games'), href='/statistics/%s/games' % league)
#         breadcrumb.children['games'].children['teams'] = MenuItem(name='Teams', href='/statistics/%s/teams' % league)
#         breadcrumb.children['game'] = MenuItem(name=_('Game'), href='#')

#     return breadcrumb

def default(request):
    last = League.objects.latest(field_name='id')
    return HttpResponseRedirect('%s%s' % (request.path, last.id))

def statistics(request, league):
    t = loader.get_template('statistics/main.html')
    l = League.objects.get(id=league)
    c = RequestContext(request, {
        'league': l,
        'leagues': League.objects.all(),
        'source': resturl(league),
        'breadcrumbs': get_breadcrums(request, league)
    })
    return HttpResponse(t.render(c))

def players(request, league):
    l = League.objects.get(id=league)
    t = loader.get_template('statistics/players.html')
    c = RequestContext(request, {
        'league': l,
        'source': resturl(league),
        'breadcrumbs': get_breadcrums(request, league)
    })
    return HttpResponse(t.render(c))

def games(request, league):
    l = League.objects.get(id=league)
    t = loader.get_template('statistics/games.html')
    c = RequestContext(request, {
        'league': l,
        'source': resturl(league),
        'breadcrumbs': get_breadcrums(request, league)
    })
    return HttpResponse(t.render(c))

def teams(request, league):
    l = League.objects.get(id=league)
    t = loader.get_template('statistics/teams.html')
    c = RequestContext(request, {
        'league': l,
        'source': resturl(league),
        'breadcrumbs': get_breadcrums(request, league)
    })
    return HttpResponse(t.render(c))

def team(request, league):
    l = League.objects.get(id=league)
    t = loader.get_template('statistics/team.html')
    c = RequestContext(request, {
        'league': l,
        'source': resturl(league),
        'breadcrumbs': get_breadcrums(request, league)
    })
    return HttpResponse(t.render(c))

def game(request, league):
    l = League.objects.get(id=league)
    t = loader.get_template('statistics/game.html')
    c = RequestContext(request, {
        'league': l,
        'source': resturl(league),
        'breadcrumbs': get_breadcrums(request, league)
    })
    return HttpResponse(t.render(c))

def players_dlg(request, league):
    l = League.objects.get(id=league)
    t = loader.get_template('statistics/players_dlg.html')
    players = Player.objects.all()
    c = RequestContext(request, {
        'league': l,
        'source': resturl(league),
        'players': players,
        'breadcrumbs': get_breadcrums(request, league)
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
