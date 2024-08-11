import pygame

class Player(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.to_sprites :list = []
        self.index : int = 0

    def update(self):
        pass
    
