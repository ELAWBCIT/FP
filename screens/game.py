# File Author: Ernest Law - A01337414

# Full library imports 
import pygame
import sys 
import toml 

# Relative file imports 
from .base import BaseScreen
from components.bird import Bird
from components.obstacles import Obstacles
from events import *
from components.textbox import Textbox
from levels import load_levels

config = toml.load('config.toml')


# Create GameScreen class, inherit from BaseScreen
class GameScreen(BaseScreen):
    def __init__(self, window, persistent=None):
        # Don't forget to call super init
        super().__init__(window, persistent)
        # Initialize bird and obstacles# Create the bird and obstacles in the constructor
        self.bird = Bird()
        self.obstacles = Obstacles()

        # This is just to get my levels for the game 
        self.level_data = load_levels()
        self.current_level = self.persistent["current level"]

        self.level_data[self.current_level - 1]
        for item in self.level_data[self.current_level - 1]:
            # position, width, height, inverted
            # print(item)
            self.obstacles.new_pipe(int(item[0]), int(item[1]), int(item[2]), int(item[3]))

        # This is for the persistent points 
        self.persistent["points"] = 0

        # To state if the game isn't lost which will run the loop - for later.
        self.lost = False
        
        # dimensions, color, bgcolor, text, font_size=36
        
        # Creation of the scorebox and then positioning it into the top right corner
        self.scorebox = Textbox((50, 50), config['color_values']['WHITE'], config['color_values']['BLACK'], "0", font_size=24)
        self.scorebox.rect.topright = (config['numeric_values']['WIDTH'], 0)
        
        # Creation of life box display, then positioning it next to scorebox at top corner
        self.lifebox = Textbox((50, 50), config['color_values']['PINK'], config['color_values']['BLACK'], self.persistent['lives'], font_size=24)
        self.lifebox.rect.topright = (config['numeric_values']['WIDTH'] - 50, 0)

        # Creation of the lost message box display for when user crashes into the floor or buildings. 
        self.lost_message = Textbox((200, 200), config['color_values']['WHITE'], config['color_values']['BLACK'], "Crash!", font_size=48)
        # This sets the message into the middle of the screen 
        self.lost_message.rect.center = self.window.get_rect().center

        # sets the timebox to be next to the lives. 
        # This is for the start time of when the game itself is starting out. This is the TOTAL time in essence
        self.start_time = pygame.time.get_ticks()
        # Need to divide by 1000 to get the seconds. Stylistic choice to round by 2 just cause I thought it looked a lot better. 
        self.timebox = Textbox((100, 50), config['color_values']['WHITE'], config['color_values']['BLACK'], str(round(self.start_time / 1000, 2)), font_size=24)
        self.timebox.rect.topright = (config['numeric_values']['WIDTH'] - 120, 0)

    # Make changes in draw, update, and manage event. 
    def update(self):
        if not self.lost:
            # To get the current time within when the gamescreen comes up
            self.current_time = pygame.time.get_ticks()
            # update the bird
            self.bird.update()
            # update the obstacles 
            self.obstacles.update()
            # Check for collisions with the pipes
            if pygame.sprite.spritecollide(self.bird, self.obstacles, dokill=False, collided=pygame.sprite.collide_mask):
                pygame.event.post(pygame.event.Event(BIRD_HIT_PIPE))
            # Check for collisions with the ground 
            if self.bird.rect.bottom >= config['numeric_values']['HEIGHT'] - 10:
                pygame.event.post(pygame.event.Event(BIRD_HIT_GROUND))
            # This is to get the time to start every single levels iteration or every failure instead of having it continuous. 
            self.timebox.text = str(round((self.current_time - self.start_time) / 1000, 2))

    
    def draw(self):
        if not self.lost:
            # Paint the window
            # Load the background image
            background_image = pygame.image.load("images/1330483.png")
            
            # Resize the background image to fit the window
            background_image = pygame.transform.scale(background_image, (config['numeric_values']['WIDTH'], config['numeric_values']['HEIGHT']))
            
            # Paint the window with the background image
            self.window.blit(background_image, (0, 0))
            
            # Draw the obstacles
            self.obstacles.draw(self.window)

            # Display the bird sprites and obstacles group 
            # resize the bird image to 100x100 pixels
            self.bird_image_resized = pygame.transform.scale(self.bird.image, (70, 70))
            self.window.blit(self.bird_image_resized, self.bird.rect)

            # Display the 80% stuff - a scorebox from persistent, the remaining lives, and the clock timer 
            self.window.blit(self.scorebox.image, self.scorebox.rect)
            self.window.blit(self.lifebox.image, self.lifebox.rect)
            self.window.blit(self.timebox.image, self.timebox.rect)
        else:
            # This will briefly show the lost message from above. 
            self.window.blit(self.lost_message.image, self.lost_message.rect)
    def manage_event(self, event):
        # This calls for the events you've already pre put within your base manage_event 
        super().manage_event(event)
        # Check for keyboard input and processes required 
        
        # If the event type is GAME_OVER 
        if event.type == GAME_OVER:
            # Take one life off of persistent 
            self.persistent['lives'] -= 1
            # If the lives value is greater than 0 - This is so my game ends when I hit 0 lives
            # Otherwise I will still have a life on numeric value 0
            if self.persistent["lives"] > 0:
                # Go to the game screen
                self.next_screen = "game"
                self.running = False
            # If I have no lives left
            else:
                # Send user to the gameover screen. 
                self.next_screen = "gameover"
                # Persistent's final points is going to be the user's final points. 
                self.final_points = self.persistent
                self.running = False

        # If the user clears the level 
        if event.type == LEVEL_CLEAR:
            self.running = False 
            # Head to the next level 
            # reload the game which will parse into the next set of levels 
            self.next_screen = "game"
            # This is to help us get to the next levels worth of numerics 
            self.persistent["current level"] += 1
            # We're going to tally the ten marks to the persistent total, this is used to calculate our final score later. 
            # Every level cleared should be + 10 points
            self.persistent['total'] += 10

        # If the user hits the ground 
        if event.type == BIRD_HIT_GROUND:
            # Self lost is set to True which kills the game loop 
            self.lost = True
            # After half a second it will go trigger the GAME_OVER event 
            pygame.time.set_timer(GAME_OVER, 500, loops=1)
        # If the user hits the pipe 
        if event.type == BIRD_HIT_PIPE:
            # Self lost is set to True which kills the game loop
            self.lost = True
            # After half a second it will go trigger the GAME_OVER event 
            pygame.time.set_timer(GAME_OVER, 500, loops=1)
        
        # If the user passes a pipe
        if event.type == BIRD_CLEARED_PIPE:
            # Add one to the points counter 
            self.persistent["points"] += 1
            # Update the scorebox text with the points 
            self.scorebox.text = self.persistent["points"]
            # Once we've gotten 10 points, we have enough to get to the next level. 
            if self.persistent["points"] == 10:
                # Trigger the LEVEL_CLEAR event so that the game goes to the next level 
                pygame.event.post(pygame.event.Event(LEVEL_CLEAR))
        
        # If the user event is a button being pressed with the button being the spacebar
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  
            # We are going to set the bird speed to -15 to get the flappy bird jumping effect. 
            self.bird.speed = -15
