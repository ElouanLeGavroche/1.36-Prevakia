import pygame
import time
import os
from functools import partial
import subprocess
import sys

import json

import random

import codecs#Pour lire l'UTF8 si l'on charge avec json des caractères spéciaux

#Importer les joueurs & mobs
from Joueur import Joueur
from Mobs import Mobs
from Bosse import Bosse

from Confirmer import Quitter

# sources externes du jeu
from src import son
from Charger import *

from projectile import Projectile


from levels import list_levels

#RENDU
from GameRender import GameRender

#clacul
from GameLogic import GameLogic

#donné intern au program
from src.objects import (
    Button,
    TextRender,
    Image,
)

pygame.init()


#Constante
FPS = 6000

SCREEN_SIZE = (900, 400)

BLOCK_SIZE = (SCREEN_SIZE[0]/45, SCREEN_SIZE[1]/20)

MENU_BOUTTON_SIZE = (118, 57)
PM_BUTTON_SIZE = (50, 50) # Plus & Moins button size

VOLUME_CHANGE = 0.1

        
class Main:
    def __init__(self):
        self.game = True
        self.ingame = False
        
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Prevakia")
        pygame.display.set_icon(load_icon())

        self.screen = pygame.display.set_mode((SCREEN_SIZE))

        self.game_logic_class = GameLogic(list_levels)
        self.game_render_class = GameRender(self.game_logic_class, self.screen)

        self.son = son

        self.get_volume = lambda: str(round(self.son.volume * 10))
        self.get_bruitage = lambda: str(round(self.son.bruitage * 10))

        self.actual_level = 0


        #CHARGEMENT OU INITIALISATION DES EFFECTS
        self.weather = ["snow", "rain", "wind"]

        self.list_effect = []
        
                
        #ECRITURE, CHARGEMENT DES DIALOGUE

        self.font = pygame.font.SysFont("monospace", 15)

    
    def load_level(self, goto):
        for i in range(len(list_levels)):
            if i == goto:
                self.actual_level = list_levels[i]
        self.actual_level.__init__()
        
    def update(self, block_positions, item_positions, background_positions):

        if self.ingame == True:
            self.game_render_class.update_weather_effect(self.actual_level.weather_effect, self.list_effect)
            self.game_render_class.update_background(background_positions)
            self.game_render_class.update_blocks(block_positions)
            self.game_render_class.update_items(item_positions)
            

                    
        fps_text = self.font.render(f"{int(self.clock.get_fps())} FPS", True, (255, 0, 0))
        self.screen.blit(fps_text, [60, 100])
    
        pygame.display.flip()
        self.clock.tick(FPS)


    def exit(self):
        """
        Permet de quitter et sauvgarder en même temps la situation actuel du joueur
        """
        self.game = False
        self.ingame = False
        
    def event(self):
        for event in pygame.event.get():
                    
                if event.type == pygame.QUIT:
                    
                    self.exit()

                elif event.type==pygame.KEYDOWN:

                    if event.key == pygame.K_d and self.ingame == True and self.game_logic_class.scroll_ar == False and self.game_logic_class.scroll_av == False:
                        self.game_logic_class.scroll_av = True
                        self.game_logic_class.scroll_tampon += SCREEN_SIZE[0]

                    if event.key == pygame.K_q and self.ingame == True and self.game_logic_class.scroll_av == False and self.game_logic_class.scroll_ar == False:
                        self.game_logic_class.scroll_ar = True
                        self.game_logic_class.scroll_tampon -= SCREEN_SIZE[0]

                
    def main(self):
        self.load_level(0)
        self.ingame = True
        
        self.game_logic_class.calculate_block_position()
        self.game_logic_class.calculate_item_position()
        self.game_logic_class.calculate_background_position()
        
        while self.game == True:
            #scroll de l'écran
            if self.game_logic_class.scroll_av == True:
                self.game_logic_class.scroll_avant()

            if self.game_logic_class.scroll_ar == True:
                self.game_logic_class.scroll_arriere()


            #éléments
            background_positions = self.game_logic_class.get_background_position()
            block_positions = self.game_logic_class.get_block_position()
            item_positions = self.game_logic_class.get_item_position()

            #effect
            self.list_effect = self.game_logic_class.calculate_weather_effect(self.list_effect, self.screen)
            #logique de jeu
                        
            
            self.event()
            self.screen.fill(0)
            self.update(block_positions, item_positions, background_positions)
            
            

main = Main()
main.main()

pygame.quit()
sys.exit()

        
