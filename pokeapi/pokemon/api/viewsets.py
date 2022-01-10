from rest_framework import viewsets
from pokemon.api import serializers
from pokemon import models

class PokemonViewset(viewsets.ModelViewSet):
    serializer_class = serializers.PokemonSerializer 
    queryset = models.Pokemon.objects.all
    