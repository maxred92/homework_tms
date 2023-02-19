from django.shortcuts import render
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import generics
from volkau_store.models import Games
from .serializers import GamesSerializer
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
