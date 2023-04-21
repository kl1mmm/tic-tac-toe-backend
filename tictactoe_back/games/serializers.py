from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('player1', 'player2', 'date', 'game_timing', 'winner')
