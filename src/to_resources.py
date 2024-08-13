import os
from typing import Union
from dotenv import load_dotenv
from game_map import GameMap
from player import Player
from pipe import Pipe

load_dotenv()

class ToResources:
    def __init__(self):
        self.to_reset()

    def get_size_to_display(self)->tuple:
        return (self.display_width, self.display_height)
        
    @staticmethod
    def get_data_env(label : str,default: Union[str,int,bool,tuple,None] = None) -> Union[str,int,tuple,bool,None]:
        data = os.getenv(key=label)

        if data is None:
            return default
        if data.lower() in ['true','false']:
            return data.lower() == 'true'
        if data.isdigit():
            return int(data)
        
        return data 
    
    def to_reset(self):
        self.display_width :int = self.get_data_env(label="SIZE_WIDTH_SCREEN")
        self.display_height :int = self.get_data_env(label="SIZE_HEIGHT_SCREEN")
        self.display_name :str = self.get_data_env(label="APP_NAME")

        self.path_pipe : str = self.get_data_env(label="PIPES")
        self.path_floor : str = self.get_data_env(label="FLOOR")
        self.path_floor_two : str = self.get_data_env(label="FLOOR_2")
        self.path_brid : str = self.get_data_env(label="BIRD_SPRITE_1")
        self.path_brid_two : str = self.get_data_env(label="BIRD_SPRITE_2")

        self.path_backgroud : str | tuple = self.get_data_env(label="BACKGROUND_SCREEN", default=(0,0,255))
        self.colors : list = [(0,0,0),(255,255,255)]

        self.game_map = GameMap(self.path_backgroud,self.path_floor, self.path_floor_two,5)
        
        self.brid = Player([self.path_brid,self.path_brid_two],self.display_width//2-50,self.display_height//2-100,(80,80),3)

        self.new_pipes()

        self.to_go = False

    def new_pipes(self):
        self.pipe_bottom = Pipe(self.path_pipe)
        self.pipe_top = Pipe(self.path_pipe,self.pipe_bottom.list_coor,True)

