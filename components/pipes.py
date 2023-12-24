# File Author: Ernest Law - A01337414

# Full library imports 
import pygame 
import random 
import toml 

# Relative file imports 
from events import *

config = toml.load('config.toml')

# Create the Pipe class and have it inherit from the pygame.sprite.Sprite
class Pipe(pygame.sprite.Sprite):
    # This is to generate the image of the pipe which in my case is buildings 
    pipe_image = pygame.image.load("images/pipe.png")
    def __init__(self, position=None, width=None, height=None, inverted=0):
        super().__init__()
        # Creation of pipe image using the image 
        self.base_image = self.pipe_image 

        # If the csv variables are all defaulted and held at None. 
        if position is None and width is None and height is None and inverted == 0:

            # Changing the properties of the pipes 
            self.image = pygame.transform.scale(self.base_image, (90, random.randint(150, 400)))

            if position is None:
                position = config['numeric_values']['HEIGHT']

            # # Create a new surface. 50w, Random int for height 
            # self.image = pygame.Surface((50, random.randint(30, SCREEN_SIZE[1] - 100)))
            
            # # Paint it with the color of your choice
            # self.image.fill((0, 255, 250))

            # Generate the rectangle that holds the image 
            self.rect = self.image.get_rect()

            # For pipe to sit on the ground, set bottom to screen height
            self.rect.bottom = config['numeric_values']['HEIGHT']

            # This was my original way to get the inversion of the pipes
            self.decider = random.choice([True, False])
            # self.rect.top = SCREEN_SIZE[self.decider]
            if self.decider == True:
                # This is what flipped the image, left up to chance on the decider variable
                self.image = pygame.transform.flip(self.image, False, True)
                # Stick the image to the top of the display 
                self.rect.y = 0

            # For pipe to appear right side of screen, set right to screen width
            self.rect.right = position
        
        else: 
            # Scale the base image of the pipe to the specified width and height
            self.image = pygame.transform.scale(self.base_image, (width, height))
            # Get the rectangle that represents the dimensions of the pipe image
            self.rect = self.image.get_rect()
            # Set the x-coordinate of the pipe's position
            self.rect.x = position
            # If the pipe is not inverted, set its bottom position to the bottom of the screen
            if not inverted:
                self.rect.bottom = config['numeric_values']['HEIGHT']
            else:
                # If the pipe is inverted, flip the image vertically
                self.image = pygame.transform.flip(self.image, False, True)
                # Set the y-coordinate of the pipe's position to the top of the screen
                self.rect.y = 0

            
    def update(self):
        # This sets the speed of the pipes, essentially moves them to the left of the screen
        self.rect.left -= 12
        # If they are less than 0 on the right value
        if self.rect.right < 0:
            # Then you kill the pipe so they disappear 
            self.kill()
            # This is to update the points for persistence 
            pygame.event.post(pygame.event.Event(BIRD_CLEARED_PIPE))



# Additional notes - used during development 

# Position, Width, Height, Inverted 
# Make the CSV files as the levels (x)
# Need to give the correct number to each section (x)

# Lives can go into Persistent (x)
# Do levels per screen (x)
# Play the same screen again instead of incrimenting a level (x)
