from django.urls import path

from .views import PokemonAPIView

urlpatterns = [
    path('pokemon/', PokemonAPIView.as_view(), name='pokemons'),
]
