
from src.game import Game
import pygame
from dotenv import load_dotenv

load_dotenv()

def main():
    pygame.init()
    game = Game()
    game.run()    

