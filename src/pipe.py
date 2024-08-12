import pygame
import random

class Pipe(pygame.sprite.Sprite):

    def __init__(self, image: str,list_coor : list = [],flip : bool = False) -> None:
        super().__init__()
        index :int = 1
        self.image = pygame.transform.scale(pygame.image.load(image),(100,700))
        self.list_coor : list = list_coor if flip and list_coor else self.get_coor()
        if flip:
            self.image = self.to_flip(self.image,False, True)
            index-=1
        self.rect = self.image.get_rect()
        self.rect.topleft = self.list_coor[index]
        self.speed : int = 1

    @staticmethod
    def to_flip(item:pygame, flip_x : bool,flip_y:bool)->pygame:
         return pygame.transform.flip(item,flip_x,flip_y)

    def get_coor(self,x_position : int = 600)->list:
        pipe_height = self.image.get_height()

        # Posición Y del pipe inferior
        pipe_bottom_y = random.randint(200, 600)
        
        # Posición Y del pipe superior (basado en la separación de 100px)
        pipe_top_y = pipe_bottom_y - pipe_height - 150
        
        return [(x_position, pipe_top_y),(x_position, pipe_bottom_y)]
        

    # def update(self):
    #     self.rect.x -= 5 
    #     if self.rect.right < 0:
    #         self.kill()  