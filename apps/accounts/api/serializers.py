from rest_framework import serializers

from apps.accounts.models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'admin', 'active', 'type']
