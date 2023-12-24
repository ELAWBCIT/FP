# File Author: Ernest Law - A01337414

# Full library imports
import pygame
import toml

# Relative file imports 
from screens.base import BaseScreen
from events import *
from components.textbox import Textbox

config = toml.load('config.toml')


# This is a custom screen to display credits from the game maker
class CreditScreen(BaseScreen):
    def __init__(self, window, persistent=None):
        # Don't forget to call super init
        super().__init__(window, persistent)
        # This is to get the background image to show up
        self.bg = pygame.transform.scale(pygame.image.load("images/1330483.png"), (config['numeric_values']['WIDTH'], config['numeric_values']['HEIGHT']))
        
        # Format: dimensions, color, bgcolor, text, font_size=36
        
        # This is to display the credits title of the game on the main menu and set it in the middle of the screen
        self.credit_box = Textbox((700, 300), config['color_values']['WHITE'], config['color_values']['BLACK'], "Credits", font_size=80)
        self.credit_box.rect.center = (config['numeric_values']['WIDTH']/2, 100)

        # This is to display the author of the game on the credit screen and set it in the middle of the screen
        self.author_box = Textbox((300, 100), config['color_values']['ORANGE'], config['color_values']['BLACK'], "By: Ernest Law - A01337414", font_size=20)
        self.author_box.rect.center = (config['numeric_values']['WIDTH']/2, 150)
        
        # This is to display the special thanks title of the game on the main menu and set it in the middle of the screen
        self.thank_box = Textbox((700, 100), config['color_values']['WHITE'], config['color_values']['BLUE'], "Special Thanks", font_size=50)
        self.thank_box.rect.center = (config['numeric_values']['WIDTH']/2, 225)

        # These are just the various credits display and again set to the middle of the screen
        self.thanks_1 = Textbox((300, 100), config['color_values']['WHITE'], config['color_values']['BLACK'], "KioNyan", font_size=20)
        self.thanks_1.rect.center = (config['numeric_values']['WIDTH']/2, 275)
        self.thanks_2 = Textbox((300, 100), config['color_values']['WHITE'], config['color_values']['BLACK'], "MannyH", font_size=20)
        self.thanks_2.rect.center = (config['numeric_values']['WIDTH']/2, 300)
        self.thanks_3 = Textbox((300, 100), config['color_values']['WHITE'], config['color_values']['BLACK'], "Kiawnu", font_size=20)
        self.thanks_3.rect.center = (config['numeric_values']['WIDTH']/2, 325)
        self.thanks_4 = Textbox((300, 100), config['color_values']['WHITE'], config['color_values']['BLACK'], "TeddyJ", font_size=20)
        self.thanks_4.rect.center = (config['numeric_values']['WIDTH']/2, 350)
        self.thanks_5 = Textbox((300, 100), config['color_values']['WHITE'], config['color_values']['BLACK'], "DL731", font_size=20)
        self.thanks_5.rect.center = (config['numeric_values']['WIDTH']/2, 375)

        # Another additional credit to Pygame
        self.pygamecredit = Textbox((500, 100), config['color_values']['MAGENTA'], config['color_values']['BLACK'], "Built via Pygame", font_size=20)
        self.pygamecredit.rect.center = (config['numeric_values']['WIDTH']/2, 450)

        # This is to display the back button and set it in the middle of the screen
        self.back_button = Textbox((150, 100), config['color_values']['CYAN'], config['color_values']['BLACK'], "BACK", font_size=50)
        self.back_button.rect.center = (config['numeric_values']['WIDTH']/2, 575)


    def manage_event(self, event):
        super().manage_event(event)
        # Thilst the program is running
        if self.running:
            # If the event type is a mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                # This is to set the click point to be on the back button
                if self.back_button.rect.collidepoint(event.pos):
                    # We set the next screen to be the welcome home screen
                    self.next_screen = "welcome"
                    self.running = False
                    

    def draw(self):
        # To draw al the textboxes that we have created
        if self.running:
            # To generate the background 
            self.window.blit(self.bg, (0, 0))
            # Generate each textbox within the sequence of code above in a linear format. 
            self.window.blit(self.credit_box.image, self.credit_box.rect)
            self.window.blit(self.author_box.image, self.author_box.rect)
            self.window.blit(self.thank_box.image, self.thank_box.rect)
            self.window.blit(self.thanks_1.image, self.thanks_1.rect)
            self.window.blit(self.thanks_2.image, self.thanks_2.rect)
            self.window.blit(self.thanks_3.image, self.thanks_3.rect)
            self.window.blit(self.thanks_4.image, self.thanks_4.rect)
            self.window.blit(self.thanks_5.image, self.thanks_5.rect)
            self.window.blit(self.pygamecredit.image, self.pygamecredit.rect)
            self.window.blit(self.back_button.image, self.back_button.rect)
