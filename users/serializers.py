from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'date_joined']

