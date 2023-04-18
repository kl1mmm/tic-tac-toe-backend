from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.Serializer):
    player1 = serializers.CharField()
    player2 = serializers.CharField()
    date = serializers.DateField(read_only=True)
    game_timing = serializers.CharField(max_length=5, read_only=True)
    winner = serializers.CharField(max_length=5, read_only=True)
