from rest_framework import serializers
from .models import PlayerStatistic
from users.serializers import UserNameSerializer


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerStatistic
        fields = ("user", "count_of_games", "count_of_wins", "count_of_loses")


class RatingSerializer(serializers.ModelSerializer):  # Сериализатор для страницы Рейтинга игроков.
    user = UserNameSerializer()

    class Meta:
        model = PlayerStatistic
        fields = ("id", "count_of_games", "count_of_wins", "count_of_loses", "user")