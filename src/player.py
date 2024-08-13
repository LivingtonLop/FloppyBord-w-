import pygame

class Player(pygame.sprite.Sprite):
    def __init__ (self, sprites : list,x :int,y:int,scale : tuple = (50,50), speed : int = 5):
        super().__init__()

        self.to_sprites :list = [pygame.transform.scale(pygame.image.load(path),scale) for path in sprites]
        self.index : int = 0
        self.image = self.to_sprites[self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed : int = speed
        self.angule : float = speed

    def update(self, pos_y):

        new = self.rect.move(0,pos_y)

        self.rect = new

        
