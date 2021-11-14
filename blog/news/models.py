from typing import ClassVar
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
import datetime
import django.utils as util


class Plan(models.Model):

    def __str__(self) -> str:
        return self.goal

    goal = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, name='author')
    text = models.CharField(max_length=100)
    start_date = models.DateField(default=util.timezone.now)
    end_date = models.DateField()
    need_money = models.IntegerField()


class AccumulateMoney(models.Model):

    day = models.IntegerField()
    income_money = models.IntegerField()
    consumption = models.IntegerField()
    plan = models.OneToOneField(Plan, on_delete=models.CASCADE, name='plan')

    def result(self) -> int:
        return (self.income_money - self.consumption) * self.day











    
