from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class LogInSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        attrs = super().validate(attrs)
        if not self.user.is_active:
            raise serializers.ValidationError("You are not allowed to login")
        attrs["full_name"] = self.user.first_name + " " + self.user.last_name
        attrs["phone_number"] = self.user.phone_number
        attrs["groups"] = [group.name for group in self.user.groups.all()]
        attrs["permissions"] = [permission.name for permission in self.user.user_permissions.all()]
        return attrs

    class Meta:
        model = User
        fields = ['username', 'password']
