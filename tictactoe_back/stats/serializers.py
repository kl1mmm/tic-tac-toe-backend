from rest_framework import serializers
from .models import PlayerStatistic


class StatsSerializer(serializers.Serializer):
    user = serializers.CharField()
    count_of_games = serializers.IntegerField(read_only=True)
    count_of_wins = serializers.IntegerField(read_only=True)
    count_of_loses = serializers.IntegerField(read_only=True)
