from rest_framework import serializers
from .models import Competition, Ring, Match, MatchResult


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Competition
        fields='__all__'

class RingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ring
        fields='__all__'

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Match
        fields='__all__'


class MatchResultSerializer(serializers.ModelSerializer):
    class Meta:
        model=MatchResult
        fields='__all__'

