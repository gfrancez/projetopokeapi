from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Pokemon
from pokemon.api.serializers import PokemonSerializer

class PokemonAPIView(APIView):
    '''
    API POKEMON TESTANDO
    '''
    def get(self, request):
        pokemons = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemons, many=True)
        return Response(serializer.data)
        