# File Author: Ernest Law - A01337414

# Full library imports
import pygame


# Event Constants:

# When the bird dies, triggers this event 
GAME_OVER = pygame.event.custom_type()

# Create a new custom event for when the bird hits the ground:
BIRD_HIT_GROUND = pygame.event.custom_type()

# Collision with pipe
BIRD_HIT_PIPE = pygame.event.custom_type()

# Avoided the pipe
BIRD_CLEARED_PIPE = pygame.event.custom_type()

# Cleared a level 
LEVEL_CLEAR = pygame.event.custom_type()
