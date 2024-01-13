import pygame


from levels import list_levels

#effect visuel
from effects import Particle


SCREEN_SIZE = (900, 400)
BLOCK_SIZE = (SCREEN_SIZE[0]/45, SCREEN_SIZE[1]/20)


class GameLogic:
    def __init__(self, list_levels):
        self.actual_level = list_levels[0]

        self.scroll = 0
        self.scroll_tampon = 0

        self.scroll_av = False 
        self.scroll_ar = False

        self.block_positions = []
        self.item_positions = []
        self.background_positions = []

    def move_position(self):
        for i in self.block_positions:
            i["x"] -= self.scroll_tampon

        for i in self.item_positions:
            i["x"] -= self.scroll_tampon

        for i in self.background_positions:
            i[1] -= self.scroll_tampon

            
    def scroll_avant(self):
        if self.scroll != self.scroll_tampon:
            self.scroll += 1
            self.move_position()
        else:
            self.scroll_av = False

    def scroll_arriere(self):
        if self.scroll != self.scroll_tampon:
            self.scroll -= 1
            self.move_position()
        else:
            self.scroll_ar = False
            
    def calculate_block_position(self):
        for row_index, row in enumerate(self.actual_level.mur):
            for col_index, block_type in enumerate(row):
                real_x = col_index * BLOCK_SIZE[0]
                real_y = row_index * BLOCK_SIZE[1]
                self.block_positions.append({"type": block_type, "x": real_x, "y": real_y})


    def calculate_item_position(self):
        for i in self.actual_level.pos_items:
            x = i[0]*BLOCK_SIZE[0]
            y = i[1]*BLOCK_SIZE[1]
            self.item_positions.append({"type": i[2], "x": x, "y": y,
                                        "id": i[3], "active": i[4]})

    def calculate_background_position(self):
        pos = 0
        for i in self.actual_level.background:
            self.background_positions.append([i, pos])   
            pos += SCREEN_SIZE[0]


    def calculate_weather_effect(self, list_effect, screen):
        for effect in list_effect:#calcul snow
                effect.move()

        new_particle = Particle.Particle(SCREEN_SIZE[0], SCREEN_SIZE[1], screen)
        list_effect.append(new_particle)

        list_effect = [particle for particle in list_effect if particle.y < SCREEN_SIZE[1]]

        return list_effect
        

    def get_item_position(self):
        return self.item_positions

    def get_block_position(self):
        return self.block_positions

    def get_background_position(self):
        return self.background_positions



