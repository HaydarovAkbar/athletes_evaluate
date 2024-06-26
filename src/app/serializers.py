from django.contrib.auth.models import Group
from rest_framework import serializers
import random
import string
from django.conf import settings

# def dehashed_password(password):
#     return make_password(password)

from account.models import User

from .models import Competition, Ring, Match, MatchResult

generate_username = lambda: ''.join(random.choice(string.ascii_lowercase) for _ in range(4)) + str(
    random.randint(10, 99))
generate_password = lambda: str(random.randint(settings.PASSWORD_BEGINING, settings.PASSWORD_END))


class UserRefereeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'ring']


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'


class RingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ring
        fields = ['competition', 'title']

    def create(self, validated_data):
        competition = validated_data['competition']

        rings = Ring.objects.all()
        ring = Ring.objects.create(title=f"ring_{len(rings) + 1}", competition=competition)

        referees_group = Group.objects.get(name='referees')
        main_referees_group = Group.objects.get(name='main_referees')
        password = '111111'
        for i in range(3):
            User.objects.create(username=generate_username(), password=password, ring=ring).groups.add(
                referees_group)
        User.objects.create(username=generate_username(), password=password, ring=ring).groups.add(
            main_referees_group)
        return ring

    def to_representation(self, instance):
        ring = super().to_representation(instance)
        referees = User.objects.filter(ring=instance).order_by('-id')
        ring['title'] = instance.competition.title

        ring["data"] = []
        for ref in referees:
            if 'referees' in ref.groups.values_list('name', flat=True):
                ring['data'] += [{'username': str(ref.username),
                                  'password': 111111,
                                  'is_main': False},
                                 ]
            else:
                ring['data'] += [{'username': str(ref.username),
                                  'password': 111111,
                                  'is_main': True},
                                 ]
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
    rings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Competition
        fields = ['title', 'description', 'is_active', 'rings']


class ActiveMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['user1', 'user2', 'ring', 'result', 'is_finished']

    def to_representation(self, instance):
        match = super().to_representation(instance)
        match['results'] = MatchResultSerializer(MatchResult.objects.filter(match=instance), many=True).data
        return match
