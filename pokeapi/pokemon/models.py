from django.db import models
from pokemon import services

class Pokemon(models.Model):
    def __init__(self, pokemon):
        self.id = services.get_id(pokemon)
        self.stats = services.get_stats(pokemon)
        self.moves = services.get_moves(pokemon)
        self.sprite = services.get_sprite(pokemon)
    
