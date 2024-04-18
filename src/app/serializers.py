from rest_framework import serializers
from .models import Competition, Ring, Match, MatchResult
import random
import string
from account.models import User

def random_char(char):
    return ''.join(random.choice(string.ascii_lowercase) for x in range(char))

def generate_key():
    return f"{random_char(4)}{random.randint(10, 99)}"


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Competition
        fields='__all__'

class RingSerializer(serializers.ModelSerializer):

    class Meta:
        model=Ring
        fields=['title', 'competition']


    def create(self, validated_data):
        title=validated_data['title']
        competition=validated_data['competition']
        ring=Ring.objects.create(title=title, competition=competition)
        for i in range(3):
            User.objects.create(username=generate_key(), password='100000')

            User.objects.create(username=generate_key(), password='100000')
        return ring
    
    def to_representation(self, instance):
        ring =  super().to_representation(instance)
        referees=User.objects.filter(ring__title=ring['title'])
        ring["data"]=[]
        for ref in referees:
            ring['data']+= [{'username':str(ref.username),
                             'password':str(ref.password)},]
        return ring
    

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Match
        fields='__all__'


class MatchResultSerializer(serializers.ModelSerializer):
    class Meta:
        model=MatchResult
        fields='__all__'

