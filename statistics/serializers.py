from statistics.models import League, Team, Game, Player, Goal, Penalty
from rest_framework import serializers


class LeagueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = League
        fields = ('name', 'from_date', 'to_date')


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('name', 'league')

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('date', 'location', 'home', 'guest', 'league')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('number', 'name', 'role', 'team', 'league')

class GoalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goal
        fields = ('time', 'game', 'team', 'player', 'assisting', 'note', 'league')

class PenaltySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Penalty
        fields = ('time', 'length', 'game', 'team', 'player', 'reason', 'note', 'league')
