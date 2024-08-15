import pygame

class UserInterface:
    def __init__(self):
        pass

    def show_score(self,display: pygame,score: int,path_background : str, coor : tuple = (230,50)):

        font = pygame.font.SysFont('Arial',30,True)
        text_top = font.render(f"Score:", True,(255,255,255))
        text_score = font.render(f"{score}", True,(255,255,255))

        background = pygame.transform.scale(pygame.image.load(path_background),(200,350))

        display.blit(background, coor)
        display.blit(text_top, (coor[0]+60,coor[1]+110))
        display.blit(text_score, (coor[0]+90,coor[1]+160))

    
    def button_option(self,display : pygame, path_btn_reset: str, path_btn_add_lead : str, path_general : str, list_coor : list):
        self.reset = pygame.transform.scale(pygame.image.load(path_btn_reset),(150,64))
        share = pygame.transform.scale(pygame.image.load(path_general),(150,64))
        lead = pygame.transform.scale(pygame.image.load(path_btn_add_lead),(360,64))

        display.blit(self.reset,list_coor[0])
        display.blit(share,list_coor[1])
        display.blit(lead,list_coor[2])
