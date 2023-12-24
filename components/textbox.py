# File Author: Timothee Guicherd - BCIT Instructor ACIT2515

import pygame  

# This is code taken from Tim's Step 4 zip file

class Textbox(pygame.sprite.Sprite):
    def __init__(self, dimensions, color, bgcolor, text, font_size=36):
        super().__init__()
        self.dimensions = dimensions
        self.color = color
        self.bgcolor = bgcolor
        self.font_size = font_size

        self.text = text
        self.update()
        

        self.rect = self.image.get_rect()

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, value):
        self._text = str(value)
        self.update()

    def update(self):
        surface = pygame.Surface(self.dimensions)
        surface.fill(self.bgcolor)

        # An additional change here to set the textboxes to be transparent 
        surface.set_colorkey(self.bgcolor)

        # Users will need to install the "Valorant" font that was included in the downloaded file. 
        font = pygame.font.SysFont("Valorant", self.font_size)
        text_surface = font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        left = self.dimensions[0] / 2 - text_rect.width / 2
        top = self.dimensions[1] / 2 - text_rect.height / 2
        surface.blit(text_surface, (left, top))
        self.image = surface
