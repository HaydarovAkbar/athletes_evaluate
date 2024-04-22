from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import Competition, Ring, Match, MatchResult
import random
import string
from account.models import User

BEGINING_NUMBER_FOR_USERNAME = 10
END_NUMBER_FOR_USERNAME = 99
LENGTH_OF_NAME = 4

PASSWORD_BEGINING = 100000
PASSWORD_END = 1000000


def random_char(char):
    return ''.join(random.choice(string.ascii_lowercase) for x in range(char))


def generate_username():
    return f"{random_char(LENGTH_OF_NAME)}{random.randint(BEGINING_NUMBER_FOR_USERNAME, END_NUMBER_FOR_USERNAME)}"


def generate_password():
    return str(random.randint(PASSWORD_BEGINING, PASSWORD_END))


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'


class RingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ring
        fields = ['competition']

    def create(self, validated_data):
        competition = validated_data['competition']

        rings = Ring.objects.all()
        ring = Ring.objects.create(title=f"ring_{len(rings) + 1}", competition=competition)

        referees_group = Group.objects.get(name='referees')
        main_referees_group = Group.objects.get(name='main_referees')
        for i in range(3):
            User.objects.create(username=generate_username(), password=generate_password(), ring=ring).groups.add(
                referees_group)
        User.objects.create(username=generate_username(), password=generate_password(), ring=ring).groups.add(
            main_referees_group)
        return ring

    def to_representation(self, instance):
        ring = super().to_representation(instance)
        referees = User.objects.filter(ring__competition=ring['competition'])

        ring["data"] = []
        for ref in referees:
            ring['data'] += [{'username': str(ref.username),
                              'password': str(ref.password)}, ]
        return ring


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'


class MatchResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchResult
        fields = '__all__'


class ActiveRingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ring
        fields = ['title', ]


class ActiveCompetitionSerializer(serializers.ModelSerializer):
    rings = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Competition
        fields = ['title', 'description', 'is_active', 'rings']
