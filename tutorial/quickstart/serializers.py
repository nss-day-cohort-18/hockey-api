from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tutorial.quickstart.models import *

class CohortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cohort
        exclude = ()



class HockeyPlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HockeyPlayer
        exclude = ()
        depth = 1

class HockeyTeamSerializer(serializers.HyperlinkedModelSerializer):
    players = HockeyPlayerSerializer(many=True, read_only=True)

    class Meta:
        model = HockeyTeam
        fields = ('url', 'teamname', 'city', 'coach', 'logo', 'mascot', 'players')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')