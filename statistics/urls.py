'''
Created on 28.6.2012

@author: teerytko
'''

from rest_framework import routers
from statistics import views

router = routers.DefaultRouter()
router.register(r'league', views.LeagueViewSet)
router.register(r'team', views.TeamViewSet)
router.register(r'game', views.GameViewSet)
router.register(r'player', views.PlayerViewSet)
router.register(r'goal', views.GoalViewSet)
router.register(r'penalty', views.PenaltyViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

from django.conf.urls import patterns, url, include
urlpatterns = patterns('',
    url(r'^$', 'statistics.views.default'),
    url(r'^rest/', include(router.urls)),
    url(r'rest/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'(?P<league>\d+)/$', 'statistics.views.league', name='league'),
    url(r'(?P<league>\d+)/game/(?P<game>\d+)/$', 'statistics.views.game',name='game'),
    url(r'(?P<league>\d+)/team/(?P<team>\d+)/$', 'statistics.views.team', name='team'),
    url(r'(?P<league>\d+)/statistics/$', 'statistics.views.statistics', name='statistics'),
)
