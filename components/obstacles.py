# File Author: Ernest Law - A01337414

# Full library imports 
import pygame 
import random

# Relative file imports  
from .pipes import Pipe


# Create the Obstacles class in it, and make sure it inherits from pygame.sprite.Group .
class Obstacles(pygame.sprite.Group):
    def __init__(self):
        # super is pygame.sprite.group. You are calling its constructor 
        super().__init__()
        # Create a new Pipe instance
        pipe = Pipe()

        # Add pipe to the group self.add
        self.add(pipe)

    def update(self):
            """
            Update the position of the pipes and add new pipes if necessary.
            """
            # Call the update method of the parent class to move the pipes
            super().update()

            # Check if there are less than 3 active pipes
            # if len(self) < 3:
            #     self.new_pipe()
            
    def new_pipe(self, position=None, width=None, height=None, inverted=0):
        # If the values of the new_pipe arguments are all going to be None/Defaulted. 
        if position is None and width is None and height is None and inverted == 0: 
            # Get the list of right coordinates of the active sprites
            right_side = [s.rect.right for s in self.sprites()]
            # Get the coordinate of the rightmost pipe
            right_max = max(right_side)
            # Add a random integer between 200 and 400 to the rightmost coordinate to get the new pipe coordinate
            new_coord = right_max + random.randint(200, 400)
            # print(new_coord)
            # Add the new pipe to the group of pipes
            self.add(Pipe(new_coord))
        else:
            # We set the new_coord which is the position x of where the pipe generates
            new_coord = position 
            # Pass in the other variables along with new_coord 
            self.add(Pipe(new_coord, width, height, inverted))

