from django.shortcuts import render
from rest_framework import generics
from .models import Plan, AccumulateMoney
from .serializers import AccumulateSerializer, PlanSerializer


class GetOnePlan(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg_= 'pk'
    serializer_class = PlanSerializer

    def get_queryset(self):
        queryset = Plan.objects.filter(author_id=self.request.user)
        return queryset
    
class ListPlans(generics.ListAPIView):
    serializer_class = PlanSerializer

    def get_queryset(self):
        queryset = Plan.objects.filter(author_id=self.request.user)
        return queryset



class GetOneAccumulate(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'pk'
    serializer_class = AccumulateSerializer

    def get_queryset(self):
        queryset = AccumulateMoney.objects.filter(plan__author=self.request.user)
        return queryset