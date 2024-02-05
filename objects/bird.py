import pygame.sprite
from layer import Layer
import assets
import configs

class Bird(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.PLAYER
        self.image = assets.get_sprite("redbird-midflap")
        self.rect = self.image.get_rect(topleft = (0, 0))
        super().__init__(*groups)
