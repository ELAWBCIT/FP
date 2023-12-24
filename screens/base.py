# File Author: Ernest Law - A01337414

# Full Library imports 
import pygame

# Relative file imports 
from components.textbox import Textbox
from events import *

# Creation of the BaseScreen class 
class BaseScreen:
    def __init__(self, window, persistent=None):
        # When I initialize my gamescreen, I need to capture the instance and time you are at when the game starts
        # Not when pygame starts, when the gamescreen starts. 

        # Compare that to the total ticks of the game 

        # This is for the persistent points. The original value is set to None
        # If persistent is None we will generate a new dictionary to store "Persisting" data values
        if persistent is None:
            self.persistent = {}
        # Otherwise assume there is an input of a custom persistent dictionary     
        else: 
            self.persistent = persistent 
        
        self.window = window
        # This is the base screen, so no next screen. It is called in our main game.py 
        self.next_screen = None
        self.running = False

    def run(self):
        # Calling the Clock from pygame 
        self.clock = pygame.time.Clock()
        # Self.lost is set to False, you are not "losing" if you are still in the game or not playing it
        self.lost = False
        # This is a variable to easily switch off our game loop later on. 
        self.running = True
        # Our while loop which servers as our game loop
        while self.running:
            # Clock tick set to 240 for performance issues on Ernest's laptop 
            self.clock.tick(240)
            # Need to update the screen and draw it
            self.update()
            self.draw()
            pygame.display.update()
            
            for event in pygame.event.get():
                self.manage_event(event)

    def draw(self):
        pass

    def update(self):
        pass

    def manage_event(self, event):
        # These are going to be the events we will loop through later on. 
        # If we are quitting the game 
        if event.type == pygame.QUIT:
            # Set self.running to False to stop the game 
            self.running = False
        # If the event type is pygame detecting a key getting pressed down
        elif event.type == pygame.KEYDOWN:
            # And if the key is the ESCAPE key
            if event.key == pygame.K_ESCAPE:
                # Set self.running to False to stop the game
                self.running = False