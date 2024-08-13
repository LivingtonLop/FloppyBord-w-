import pygame
from to_resources import ToResources

class Game (ToResources):
    def __init__(self):
        super().__init__()
        size : tuple = self.get_size_to_display() 
        self.events_key = [pygame.K_SPACE, pygame.K_RETURN, pygame.K_j]
        
        self.display = pygame.display.set_mode(size=size)
        pygame.display.set_caption(self.display_name)

        self.to_execute : bool = True
        self.to_clock = pygame.time.Clock()
        self.fps : float = 60.0
        self.score : int = 0
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.brid)

        self.all_pipes = pygame.sprite.Group()
        self.add_new_pipes()


        # self.game_map.load_pipes()

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

            if event.type == pygame.KEYDOWN:
                if event.key in self.events_key:
                    self.brid.update(-self.brid.speed*20)
                    self.to_go = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    self.brid.update(-self.brid.speed*20)
                    self.to_go = True
            

    def update(self):
        if self.to_go:
            self.brid.update(self.brid.speed)
            
            for pipe in self.all_pipes:
                pipe.rect.x -= pipe.speed
                if pipe.rect.right < 0:
                    pipe.kill()
                
            if pipe.rect.x == self.brid.rect.x:    
                self.new_pipes()
                self.add_new_pipes()
            
                    
            
        if self.game_map.confirm_collision(self.brid,self.all_pipes, self.display.get_height()):
            pass


    def render(self):
        self.display.fill((self.colors[1]))
        
        # self.show_hit_box(self.display,self.brid.rect,(0,255,0))
        # self.show_hit_box(self.display,self.pipe_bottom.rect)
        # self.show_hit_box(self.display,self.pipe_top.rect)

        self.game_map.render(self.display)
        self.all_pipes.draw(self.display)
        self.all_sprites.draw(self.display)        

        pygame.display.update()
    
    @staticmethod
    def show_hit_box(display : pygame ,rect_entity : tuple, color : tuple = (255, 0, 0)):
        pygame.draw.rect(display,color, rect_entity, 2)

    def add_new_pipes(self):
        self.all_pipes.add(self.pipe_bottom)
        self.all_pipes.add(self.pipe_top)
        print(self.all_pipes)