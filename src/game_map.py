import pygame
from player import Player
from pipe import Pipe

class GameMap:
    
    def __init__(self,background : str | tuple, backgrass : str, movegrass : str, speed :int):
        self.to_background = pygame.image.load(background) if type(background) is not tuple else background  
        # self.to_pipe = self.to_scale(pygame.image.load(pipe),(100,700)) 
        self.to_backgrass = self.to_scale(pygame.image.load(backgrass),(650,50))
        self.to_movegrass = self.to_scale(pygame.image.load(movegrass),(50,50))  
        self.speed : int = speed
        # self.list_pipes : list = []
        self.list_move_grass : list = [] 
        
    @staticmethod
    def to_scale(item : pygame ,scale : tuple) -> pygame:
        return pygame.transform.scale(item,scale)
    
    @staticmethod
    def confirm_collision(player : Player, pipe : Pipe, display_height : int )-> bool:
        res = False
        if pygame.sprite.spritecollide(player,pipe,False):
            res = True
        if player.rect.top <= 0 or player.rect.bottom >= display_height:
            res = True

        return res
    

    def move_grass(self, screen:pygame):
        """Genera y mueve el césped sobre el fondo para simular el movimiento."""
        screen_width =screen.get_width()
        grass_width = self.to_movegrass.get_width()

        # Inicializar la posición del césped si la lista está vacía
        if not self.list_move_grass:
            for i in range(screen_width // grass_width + 2):
                self.list_move_grass.append(i * grass_width)

        # Mover el césped
        for i in range(len(self.list_move_grass)):
            self.list_move_grass[i] -= self.speed
            if self.list_move_grass[i] <= -grass_width:
                self.list_move_grass[i] = screen_width

        # Dibujar el césped en la pantalla
        for position in self.list_move_grass:
            screen.blit(self.to_movegrass, (position, screen.get_height() - self.to_movegrass.get_height()))

    # def draw_pipes(self, screen : pygame):
    #     """Dibuja los pipes en la pantalla."""
    #     for index, (x, y) in enumerate(self.list_pipes):
    #         if index > 0 and index%2 == 1:
    #             screen.blit(self.to_flip(self.to_pipe,0,90), (x, y))
    #         else:
    #             screen.blit(self.to_pipe,(x,y))

    def render(self, display : pygame):
        if type(self.to_background) is tuple:
            display.fill(self.to_background)
        else:
            self.to_background = pygame.transform.scale(self.to_background,display.get_size())
            display.blit(self.to_background,(0,0))
        
        #load
        display.blit(self.to_backgrass,(0,650))
        self.move_grass(display)
        

