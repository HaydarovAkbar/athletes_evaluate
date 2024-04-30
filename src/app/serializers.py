from django.contrib.auth.models import Group
from rest_framework import serializers
import random
import string
from django.conf import settings

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
        for i in range(3):
            # User.objects.create(username=generate_username(), password=generate_password(), ring=ring).groups.add(
            #     referees_group)
            user_referee = UserRefereeSerializer.create(username=generate_username(), password=generate_password(), ring=ring)
            user_referee.groups.add(referees_group)
        # User.objects.create(username=generate_username(), password=generate_password(), ring=ring).groups.add(
        #     main_referees_group)
        main_user = UserRefereeSerializer.create(username=generate_username(), password=generate_password(), ring=ring)
        main_user.groups.add(main_referees_group)
        return ring

    def to_representation(self, instance):
        ring = super().to_representation(instance)
        referees = User.objects.filter(ring=instance).order_by('-id')
        ring['title'] = instance.competition.title

        ring["data"] = []
        for ref in referees:
            if 'referees' in ref.groups.values_list('name', flat=True):
                ring['data'] += [{'username': str(ref.username),
                                  'password': str(ref.password),
                                  'is_main': False},
                                 ]
            else:
                ring['data'] += [{'username': str(ref.username),
                                  'password': str(ref.password),
                                  'is_main': True},
                                 ]
        return ring


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

    def create(self, validated_data):
        match = self.Meta.model.objects.create(**validated_data)
        users = User.objects.filter(ring=match.ring, is_active=True)
        for user in users:
            if 'referees' in user.groups.values_list('name', flat=True):
                MatchResult.objects.create(match=match, referee=user)
        return match


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
