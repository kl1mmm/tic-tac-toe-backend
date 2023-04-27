from rest_framework import serializers

from users.serializers import UserNameSerializer
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('player1', 'player2', 'date', 'game_timing', 'winner')


class GameInfoSerializer(serializers.ModelSerializer):
    p1Info = UserNameSerializer(source='player1')
    p2Info = UserNameSerializer(source='player2')

    class Meta:
        model = Game
        fields = ('id', 'date', 'game_timing', 'winner', 'p1Info', 'p2Info')
