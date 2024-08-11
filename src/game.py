import pygame
from to_resources import ToResources

class Game (ToResources):
    def __init__(self):
        super().__init__()
        size : tuple = self.get_size_to_display() 
        
        self.display = pygame.display.set_mode(size=size)
        pygame.display.set_caption(self.display_name)

        self.to_execute : bool = True
        self.to_clock = pygame.time.Clock()
        self.fps : float = 60.0
        self.score : int = 0
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.brid)

    def run(self):
        while self.to_execute:
            self.events()
            self.update()
            self.render()
            self.to_clock.tick(self.fps)
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.to_execute = False

    def update(self):
        self.all_sprites.update()

    def render(self):
        self.display.fill((self.colors[1]))
        
        self.game_map.render(self.display)
        self.all_sprites.draw(self.display)

        pygame.display.update()