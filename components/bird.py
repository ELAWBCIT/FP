# File Author: Ernest Law - A01337414

# Full library imports
import pygame 
import toml 

# Relative file imports 
from events import *

config = toml.load('config.toml')


# Create the class Bird
# It must inherit from pygame.sprite.Sprite 
class Bird(pygame.sprite.Sprite):
    bird_image = pygame.image.load("images/hornet2.png")
    def __init__(self):
        '''
        Load the bird image 
        Resize it to a decent size (100x100 pixels)
        Add a speed attribute with initial value of 0 - vertical speed of bird
        '''
        super().__init__()
        # Setting a new self variable...
        self.base_image = self.bird_image
        # So that it can be transformed and scaled down
        self.image = pygame.transform.scale(self.base_image, (70, 70))
        # Getting the rectangular area of where the bird will occupy 
        self.rect = self.image.get_rect()
        # Setting up the numeric value of the speed attribute to the bird 
        self.speed = 0 
    
    # Create the update method
    def update(self):
        # Make sure the bird falls down

        # Incrimenting the speed attribute with +1 per update when called
        self.speed += 1
        # Increasing the y coordinate of the bird sprite, this is for the bird to fall down the screen
        self.rect.bottom = self.rect.bottom + self.speed 

        # Make sure the bird stays on the screen 
        if self.rect.bottom > config['numeric_values']['HEIGHT']:
            self.rect.bottom = config['numeric_values']['HEIGHT']
            # Create custom event when the bird falls to the ground
            pygame.event.post(pygame.event.Event(BIRD_HIT_GROUND))
        
        # If the bird is flying up, make sure it doesn't fly too high
        if self.rect.top < 0:
            # Don't want the bird to disappear out of the confines of the display window 
            self.rect.top = 0
