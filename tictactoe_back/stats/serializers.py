from rest_framework import serializers
from .models import PlayerStatistic


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerStatistic
        fields = ("user", "count_of_games", "count_of_wins", "count_of_loses")
