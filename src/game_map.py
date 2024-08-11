import pygame

class GameMap:
    
    def __init__(self,background : str | tuple, pipe : str, backgrass : str, movegrass : str):
        
        print(background)
        self.to_background = pygame.image.load(background) if type(background) is not tuple else background  
        self.to_pipe = self.to_scale(pygame.image.load(pipe),(100,100))  
        self.to_backgrass = pygame.image.load(backgrass)
        self.to_movegrass = pygame.image.load(movegrass)  

    @staticmethod
    def to_scale(item : pygame ,scale : tuple) -> pygame:
        return pygame.transform.scale(item,scale)

    def render(self, display : pygame):
        if type(self.to_background) is tuple:
            display.fill(self.to_background)
        else:
            self.to_background = pygame.transform.scale(self.to_background,display.get_size())
            display.blit(self.to_background,(0,0))
        #render items
        display.blit(self.to_pipe,(200,0))
        display.blit(self.to_backgrass,(300,0))
        display.blit(self.to_movegrass,(200,0))

