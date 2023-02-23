from django.shortcuts import render
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import generics
from rest_framework import filters as rest_filters
from django_filters import rest_framework as filters
from volkau_store.models import Games, Category
from .serializers import GamesSerializer, CategorySerializer


import random


# Create your views here.

class GamesList(generics.ListAPIView):
    
    serializer_class = GamesSerializer
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def get_queryset(self):
        queryset = Games.objects.all()
        random_games = random.randrange(0,  queryset.count() - 1)
        value = self.request.query_params.get('random')
        if value == 'True':
            return queryset.filter(id=random_games)
        else:
            return queryset
            

class GetCategoryGameInfoView(generics.ListAPIView):
    
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    serializer_class = GamesSerializer
    
    def get_queryset(self):
        category = self.kwargs['category']
        return Games.objects.filter(category__title=category.title())


class GetGameInfoFilterView(generics.ListAPIView):

    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['category__title',]

class GetGameInfoSearchView(generics.ListAPIView):

    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    filter_backends = [rest_filters.SearchFilter]
    search_fields = ['name',]


class GetGameInfoOrderView(generics.ListAPIView):

    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    filter_backends = [rest_filters.OrderingFilter]
    ordering_fields = ['name', 'release_date', 'price']

