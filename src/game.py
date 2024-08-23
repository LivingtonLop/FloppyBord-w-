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
        
        self.all_pipes = pygame.sprite.Group()
        
        self.list_coor_ui: list = [ 
                                    (140,400), #reset
                                    (350,400), #share
                                    (140,500) #add score
                                ]

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

            if not self.to_pause:
                # print(f"En ejecucion{self.to_pause}")

                if event.type == pygame.KEYDOWN:
                    if event.key in self.events_key:
                        self.brid.update(-self.brid.speed*20)
                        self.to_go = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        self.brid.update(-self.brid.speed*20)
                        self.to_go = True
            else :
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_x, mouse_y = event.pos
                        btn_x, btn_y = self.list_coor_ui[0]            
                        if btn_x <= mouse_x <= btn_x + self.ui.reset.get_width() and btn_y <= mouse_y <= btn_y + self.ui.reset.get_height():
                            self.to_reset()
                            self.score = 0
                            self.all_pipes.empty()
                            self.all_sprites.empty()


    def update(self):
        if len(self.all_sprites) == 0 and len(self.all_pipes) == 0:
            self.all_sprites.add(self.brid)
            self.add_new_pipes()

        if self.to_go:
                
            self.brid.update(self.brid.speed)
            
            for pipe in self.all_pipes:
                pipe.rect.x -= pipe.speed
                if pipe.rect.right < 0:
                    pipe.kill()
                
            if pipe.rect.x == self.brid.rect.x:    
                self.new_pipes()
                self.add_new_pipes()
                self.score+=1

        if self.game_map.confirm_collision(self.brid,self.all_pipes, self.display.get_height()):
            self.to_go = False
            self.to_pause = True
 

    def render(self):
        self.display.fill((self.colors[1]))
        
        # self.show_hit_box(self.display,self.brid.rect,(0,255,0))
        # self.show_hit_box(self.display,self.pipe_bottom.rect)
        # self.show_hit_box(self.display,self.pipe_top.rect)

        self.game_map.render(self.display)
        self.all_pipes.draw(self.display)
        self.ui.show_score_in_game(self.display,self.score)
        self.all_sprites.draw(self.display)        

        if self.to_pause:
            self.ui.show_score(self.display,self.score,self.path_score_background)
            self.ui.button_option(self.display,self.path_btn_reset,self.path_btn_lead,self.path_btn_share,self.list_coor_ui)


        pygame.display.update()
    
    @staticmethod
    def show_hit_box(display : pygame ,rect_entity : tuple, color : tuple = (255, 0, 0)):
        pygame.draw.rect(display,color, rect_entity, 2)

    def add_new_pipes(self):
        self.all_pipes.add(self.pipe_bottom)
        self.all_pipes.add(self.pipe_top)
        #print(self.all_pipes)