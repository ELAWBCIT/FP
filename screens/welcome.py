# File Author: Ernest Law - A01337414

# Full library imports 
import pygame
import toml 

# Relative file imports 
from screens.base import BaseScreen
from events import *
from components.textbox import Textbox

config = toml.load('config.toml')


# Create the WelcomeScreen class, inherit from BaseScreen
class WelcomeScreen(BaseScreen):
    def __init__(self, window, persistent=None):
        # Don't forget to call super init 
        super().__init__(window, persistent)
        # This is to get the background image to show up 
        self.bg = pygame.transform.scale(pygame.image.load("images/1330483.png"), (config['numeric_values']['WIDTH'],config['numeric_values']['HEIGHT']))
        
        # Format: dimensions, color, bgcolor, text, font_size=36
        
        # This is to display the title of the game on the main menu and set it in the middle of the screen
        self.title_box = Textbox((700, 300), config['color_values']['WHITE'], config['color_values']['BLACK'], "FLAPPY HORNET", font_size=80)
        self.title_box.rect.center = (config['numeric_values']['WIDTH']/2, 100)

        # This is to display the author of the game on the main menu and set it in the middle of the screen
        self.author_box = Textbox((300, 100), config['color_values']['WHITE'], config['color_values']['BLACK'], "By: Ernest Law - A01337414", font_size=20)
        self.author_box.rect.center = (config['numeric_values']['WIDTH']/2, 250)
        
        # This is to display the start button and set it in the middle of the screen
        self.start_button = Textbox((170, 50), config['color_values']['CYAN'], config['color_values']['BLUE'], "PLAY", font_size=50)
        self.start_button.rect.center = (config['numeric_values']['WIDTH']/2, 450)

        # This is to display the MOTD and set it in the middle of the screen
        self.motto = Textbox((500, 50), config['color_values']['WHITE'], config['color_values']['BLUE'], "Dedicated to you, our future pioneers...", font_size=12)
        self.motto.rect.center = (config['numeric_values']['WIDTH']/2, 575)

    def manage_event(self, event):
        super().manage_event(event)
        # Whilst the program is running
        if self.running:
            # If the event type is a mouse click 
            if event.type == pygame.MOUSEBUTTONDOWN:
                # This is to set the click point to be on the start button
                if self.start_button.rect.collidepoint(event.pos):
                    # We set the next screen to be the game screen again
                    self.next_screen = "game"
                    # As this is the starting point, we need to set the values to be instantiated
                    self.persistent['lives'] = 3
                    self.persistent['current level'] = 1
                    self.persistent['total'] = 0
                    self.running = False
                # A secret credits menu, this is to set the click point to be on the MOTD
                if self.motto.rect.collidepoint(event.pos):
                    # We set the next screen to be the credits screen. 
                    self.next_screen = "credits"
                    self.running = False
                    

    def draw(self):
        # To draw all the textboxes that we have created
        if self.running:
            # To generate the background
            self.window.blit(self.bg, (0, 0))
            # Generate each textbox within the sequence of code above in a linear fashion.
            self.window.blit(self.title_box.image, self.title_box.rect)
            self.window.blit(self.author_box.image, self.author_box.rect)
            self.window.blit(self.start_button.image, self.start_button.rect)
            self.window.blit(self.motto.image, self.motto.rect)
