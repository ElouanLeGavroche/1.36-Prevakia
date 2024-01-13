import pygame
from Charger import *

#effect visuel
from effects import Particle

SCREEN_SIZE = (900, 400)
BLOCK_SIZE = (SCREEN_SIZE[0]/45, SCREEN_SIZE[1]/20)


class GameRender:
    def __init__(self, game_logic, screen):
        self.game_logic = game_logic
        self.screen = screen

        self.blocks = [
            load_block(),
            load_block("cube", BLOCK_SIZE),
            load_block("porte", BLOCK_SIZE),
            load_block("support", BLOCK_SIZE),
            load_block("echelle", BLOCK_SIZE),
            load_block("pente", BLOCK_SIZE),
            load_block("pente_2", BLOCK_SIZE),
            load_block("pente_3", BLOCK_SIZE),
            load_block("cube_bloquer", BLOCK_SIZE),
            load_block("barille_centre", BLOCK_SIZE),
            load_block("munition", BLOCK_SIZE),
            load_block("bois", BLOCK_SIZE),
            load_block("bois_broken", BLOCK_SIZE)
    
            ]

        self.backgrounds = [
            load_background("fond_opti", (SCREEN_SIZE[0]*3, SCREEN_SIZE[1])),
            load_background("fond_plan_1", (SCREEN_SIZE[0], SCREEN_SIZE[1])),
            load_background("game_over", (SCREEN_SIZE[0], SCREEN_SIZE[1])),
            load_background("menu_echap_fond", (SCREEN_SIZE[0], SCREEN_SIZE[1])),    

            ]

        self.items = [
            load_item(),
            load_item("cle", (BLOCK_SIZE[0], BLOCK_SIZE[1])),
            load_item("porte_fermer", (BLOCK_SIZE[0], BLOCK_SIZE[1]*3)),
            load_item("porte_ouverte", (BLOCK_SIZE[0], BLOCK_SIZE[1]*3)),
            load_item("grappin", (BLOCK_SIZE[0], BLOCK_SIZE[1])),
            load_item("hache", (BLOCK_SIZE[0]/2, BLOCK_SIZE[1])),
            load_item("generateur_on", (BLOCK_SIZE[0]*3, BLOCK_SIZE[1]*3)),
            load_item("generateur_off", (BLOCK_SIZE[0]*3, BLOCK_SIZE[1]*3)),
            load_item("lumiere"),
            load_item("flux_lumiere"),
            load_item("bouclier_on", (BLOCK_SIZE[0]*3.5, BLOCK_SIZE[1]*3.5)),
            load_item("bouclier_off", (BLOCK_SIZE[0]*3.5, BLOCK_SIZE[1]*3.5)),
            load_item("prevakia", (BLOCK_SIZE[0]*7, BLOCK_SIZE[1]*2.5))
            ]
        
    def update_background(self, background_positions):
        for item_info in background_positions:
            self.screen.blit(self.backgrounds[item_info[0]],(item_info[1],0))
            
    def update_items(self, item_positions):
        for item_info in item_positions:
            item_type = item_info["type"]
            pos_x = item_info["x"]
            pos_y = item_info["y"]

            if 0 < item_type < len(self.items):
                self.screen.blit(self.items[item_type][0], (pos_x, pos_y))
        
    def update_blocks(self, block_positions):
        for block_info in block_positions:
            block_type = block_info["type"]
            pos_x = block_info["x"]
            pos_y = block_info["y"]

            if 0 < block_type < len(self.blocks):
                self.screen.blit(self.blocks[block_type][0], (pos_x, pos_y))

    def update_weather_effect(self, type_weather, list_effect):
        for element in list_effect:
            element.draw()