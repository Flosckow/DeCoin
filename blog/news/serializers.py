from typing import ClassVar

from django.contrib.auth.models import User
from django.db import models
from .models import AccumulateMoney, Plan
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class PlanSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Plan
        fields = '__all__'

class AccumulateSerializer(serializers.ModelSerializer):
    plan = PlanSerializer(read_only=True)

    class Meta:
        model = AccumulateMoney
        fields = '__all__'