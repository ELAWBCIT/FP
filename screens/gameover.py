# File Author: Ernest Law - A01337414

# Full library imports
import pygame 
import toml 

# Relative file imports 
from screens.base import BaseScreen
from events import *
from components.textbox import Textbox

config = toml.load('config.toml')


# Create the GameOverScreen class, inherit from BaseScreen
class GameOverScreen(BaseScreen):
    def __init__(self, window, persistent=None):
        # Don't fogrget to call super init
        super().__init__(window, persistent)
        # This is to get the background image to show up 
        self.bg = pygame.transform.scale(pygame.image.load("images/1330483.png"), (config['numeric_values']['WIDTH'], config['numeric_values']['HEIGHT']))
        
        # Format: dimensions, color, bgcolor, text, font_size=36
        
        # This is to display the loss message and set it in the middle of the screen
        self.lose_box = Textbox((500, 250), config['color_values']['WHITE'], config['color_values']['BLACK'], "GAME OVER!", font_size=72)
        self.lose_box.rect.center = (config['numeric_values']['WIDTH']/2, 150)

        # This is to display the final score and set it in the middle of the screen 
        # Points are calculated with the total (10 per level cleared) and the points gained in the level user died in
        self.final_points = persistent['total'] + persistent['points']
        self.final_point = Textbox((300, 100), config['color_values']['WHITE'], config['color_values']['BLACK'], f'Final Score: {self.final_points}', font_size=28)
        self.final_point.rect.center = (config['numeric_values']['WIDTH']/2, 250)

        # This is to display the restart button and set it in the middle of the screen
        self.restart_button = Textbox((200, 50), config['color_values']['ORANGE'], config['color_values']['BLUE'], "REPLAY", font_size=24)
        self.restart_button.rect.center = (config['numeric_values']['WIDTH']/2, 375)

        # This is to display the main menu button and set it in the middle of the screen
        self.menu_button = Textbox((175, 50), config['color_values']['WHITE'], config['color_values']['BLUE'], "MAIN MENU", font_size=24)
        self.menu_button.rect.center = (config['numeric_values']['WIDTH']/2, 420)

        # This is to display the quit button and set it in the middle of the screen 
        self.quit_button = Textbox((175, 50), config['color_values']['PINK'], config['color_values']['BLUE'], "QUIT", font_size=24)
        self.quit_button.rect.center = (config['numeric_values']['WIDTH']/2, 550)
    
    def manage_event(self, event):
        super().manage_event(event)
        # Whilst the program is running
        if self.running:
            # If the event type is a mouse click 
            if event.type == pygame.MOUSEBUTTONDOWN:
                # This is to set the click point to be on the restart button
                if self.restart_button.rect.collidepoint(event.pos):
                    # We set the next screen to be the game screen again 
                    self.next_screen = "game"
                    # As this is the starting point, we need to set the values to be instantiated in the screens/games.py
                    self.persistent['lives'] = 3
                    self.persistent['current level'] = 1
                    self.persistent['total'] = 0
                    self.running = False
                # This is to set the click point to be on the menu button
                if self.menu_button.rect.collidepoint(event.pos):
                    # It will take you back to the welcome screen
                    self.next_screen = "welcome"
                    self.running = False
                # This is to set the click point to be on the quit button 
                if self.quit_button.rect.collidepoint(event.pos):
                    # The program will just stop at this point. 
                    self.running = False 
    
    def draw(self):
        # To draw all the textboxes that we have created
        if self.running:
            # To generate the background 
            self.window.blit(self.bg, (0, 0))
            # Generate each textbox within the sequence of code above in a linear fashion. 
            self.window.blit(self.lose_box.image, self.lose_box.rect)
            self.window.blit(self.final_point.image, self.final_point.rect)
            self.window.blit(self.restart_button.image, self.restart_button.rect)
            self.window.blit(self.menu_button.image, self.menu_button.rect)
            self.window.blit(self.quit_button.image, self.quit_button.rect)
