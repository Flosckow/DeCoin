from django.contrib import admin
from django.urls import path, include
from .views import GetOneAccumulate, GetOnePlan, ListPlans



urlpatterns = [
    path('one_plan/<int:pk>', GetOnePlan.as_view(), name='get_one_plan'),
    path('all_plans', ListPlans.as_view(), name='all_plan'),
    path('one_acc/<int:pk>', GetOneAccumulate.as_view(), name='get_one accumulate')
]