from rest_framework import serializers
from .models import PlayerStatistic


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerStatistic
        fields = '__all__'
