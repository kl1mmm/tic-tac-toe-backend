from rest_framework import serializers
from .models import PlayerStatistic


class StatsSerializer(serializers.Serializer):
    user = serializers.CharField()
    count_of_games = serializers.IntegerField(read_only=True)
    count_of_wins = serializers.IntegerField(read_only=True)
    count_of_loses = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return PlayerStatistic.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get("user", instance.user)
        instance.count_of_games = validated_data.get("count_of_games", instance.count_of_games)
        instance.count_of_wins = validated_data.get("count_of_wins", instance.count_of_wins)
        instance.count_of_loses = validated_data.get("count_of_loses", instance.count_of_loses)
        instance.save()
        return instance
