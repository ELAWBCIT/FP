# File Author: Ernest Law - A01337414

# Full library imports 
import pygame
import toml

# Relative file imports - mostly pertaining to screens with 1 constants file 
from screens.game import GameScreen
from screens.welcome import WelcomeScreen 
from screens.gameover import GameOverScreen
from screens.credits import CreditScreen

# This is to read the configuration file from toml 
def toml_reader():
    try:
        with open("config.toml", "r") as file:
            config = toml.load(file)
    except FileNotFoundError:
        print('Failed to find toml file, please check your game folders for - config.toml')
        config = {}
    return config 

# The main function which will start the code 
def main():
    '''
    main will run the event loop and display our sprites
    '''
    # initialize pygame with pygame.init()
    pygame.init()

    # create the main window with pygame.display.set_mode via decent size of 800 x 600
    config = toml_reader()
    window = pygame.display.set_mode((config.get("numerical_values", {}).get("WIDTH", 800), config.get("numerical_values", {}).get("HEIGHT", 600)))

    # This is a dictionary for all the screens that are displayed throughout the game 
    screens = {
        "welcome": WelcomeScreen,
        "game": GameScreen,
        "gameover": GameOverScreen,
        "credits": CreditScreen,
    }

    # This is the current screen that will be shown to the user 
    current_screen = "welcome"

    # Initialize persistent before the loop begins 
    persistent = {}

    # The first game loop, set based on the variable here. 
    # This code is partially from Instructor Timothee Guicherd. 
    running = True
    while running:
        screen_class = screens[current_screen]
        # Need to put window and persistent into my screen 
        screen = screen_class(window, persistent)
        screen.run()

        if screen.next_screen:
            current_screen = screen.next_screen
            persistent = screen.persistent
        else:
            running = False
        
# Main guard as standard convention. 
if __name__ == '__main__':
    main()
