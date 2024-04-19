from rest_framework import serializers
from .models import Competition, Ring, Match, MatchResult
import random
import string
from account.models import User

BEGINING_NUMBER=10
END_NUMBER=99
LENGTH_OF_NAME=4

PASSWORD_BEGINING=100000
PASSWORD_END=1000000

def random_char(char):
    return ''.join(random.choice(string.ascii_lowercase) for x in range(char))


def generate_username():
    return f"{random_char(LENGTH_OF_NAME)}{random.randint(BEGINING_NUMBER, END_NUMBER)}"

def generate_password():
    return str(random.randint(100000))

class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Competition
        fields='__all__'

class RingSerializer(serializers.ModelSerializer):

    class Meta:
        model=Ring
        fields=['competition']


    def create(self, validated_data):
        competition=validated_data['competition']
        rings=Ring.objects.all()
        ring=Ring.objects.create(title=f"ring_{len(rings)+1}", competition=competition)
        for i in range(3):
            User.objects.create(username=generate_username(), password=generate_password(), ring=ring)

            User.objects.create(username=generate_username(), password=generate_password(), ring=ring)
        return ring
    
    def to_representation(self, instance):
        ring =  super().to_representation(instance)
        referees=User.objects.filter(ring__competition=ring['competition'])
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

