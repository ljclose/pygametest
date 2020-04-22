#!/usr/bin/env python
#
#
#
#
#

# documentation string of this module
"""
Minimal pygame program.
"""
# some informational variables
__author__    = "$Author: DR0ID $"
__version__   = "$Revision: 109 $"
__date__      = "$Date: 2007-04-03 18:00:40 +0200 (Di, 03 Apr 2007) $"
__license__   = ''
__copyright__ = "DR0ID (c) 2007   http://mypage.bluewin.ch/DR0ID"

#----------------------------- actual code --------------------------------

# import the pygame module, so you can use it
import pygame

# define a main function
def main():
    
    # initialize the pygame module
    pygame.init()
    
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((288,175))

    # load image
    image = pygame.image.load("pikachusprite50x50.png")
    bgd_image = pygame.image.load("background.jfif")

    #blit background
    screen.blit(bgd_image, (0,0))

    # blit image
    screen.blit(image, (75,125))

    # flip/update display
    pygame.display.flip()

    # define screen width and height
    screen_width = 288
    screen_height = 175

    # define position of Pikachu image
    xpos = 75
    ypos = 125
    
    # how many pixels Pikachu moves each frame
    step_x = 5
    step_y = 5

    # check if Pikachu is still on screen, if not change direction
    if xpos>screen_width-50 or xpos<0:
        step_x = -step_x
    if ypos>screen_height-50 or ypos<0:
        step_y = -step_y
    # update the position of the smiley
    xpos += step_x # move it to the right
    ypos += step_y # move it down

    # erase the screen
    screen.blit(bgd_image, (0,0))
    # now blit the smiley on screen
    screen.blit(image, (xpos, ypos))
    # and update the screen
    pygame.display.flip()

    # define a variable to control the main loop
    running = True
    
    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event if of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
    
    
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()