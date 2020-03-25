from django.contrib.auth.models import User, Group
from rest_framework import serializers
from mainapp.models import UserInfo


class UserInfoSerializer(serializers.Serializer):
    class Meta:
        model = UserInfo
        fields = '__all__'