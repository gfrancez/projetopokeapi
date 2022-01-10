from rest_framework import serializers
from pokemon import models

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Pokemon
        fields = '__all__'