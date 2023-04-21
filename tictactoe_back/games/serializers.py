from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.Serializer):
    player1 = serializers.CharField()
    player2 = serializers.CharField()
    date = serializers.DateField(read_only=True)
    game_timing = serializers.CharField(max_length=5, read_only=True)
    winner = serializers.CharField(max_length=5, read_only=True)

    def create(self, validated_data):
        return Game.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.player1 = validated_data.get("player1", instance.player1)
        instance.player2 = validated_data.get("player2", instance.player2)
        instance.date = validated_data.get("date", instance.date)
        instance.game_timing = validated_data.get("game_timing", instance.game_timing)
        instance.winner = validated_data.get("winner", instance.winner)
        instance.save()
        return instance
