import pygame

import os
import math
from planets_class_00 import Planet

os.system('cls')

pygame.init()

WIDTH, HEIGHT = (1300, 900)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
Planet.WIDTH = WIDTH
Planet.HEIGHT = HEIGHT

# create TEXT for visible SCREEN output
program_title = "Newtonian Orbital Simulation of the Inner Planets"
title_text = Planet.FONT_CS_36.render(program_title, True, Planet.WHITE)
abigail_text = Planet.FONT_CS_36.render("By: Abigail Lightle", True, Planet.WHITE)
text_stats = Planet.FONT_LST_32.render("Distance from the Sun", True, Planet.BLACK)
text_shortcuts = Planet.FONT_LST_32.render("Keyboard Shortcuts", True, Planet.BLACK)
text_gravity = Planet.FONT_LST_32.render("Law of Gravitation", True, Planet.BLACK)

# create images for visible SCREEN output
img_background = pygame.image.load("stars.jpg").convert()
img_newton = pygame.image.load("Newtons_Gravity_Law.png")

# Create Planets and Sun
# def __init__(self, name, x, y, relative_radius, color, mass, y_vel):
sun = Planet("Sun", 0, 0, 2.5, Planet.YELLOW, 1.98892E30, 0)
mercury = Planet("Mercury", -0.387, 0, 0.376, Planet.DARK_GRAY, 3.30e23, 47000)
venus = Planet("Venus", -0.723, 0, 0.949, Planet.WHITE, 4.87E24, 35020)
earth = Planet("Earth", -1, 0, 1.0, Planet.BLUE, 5.97E24, 29783)
mars = Planet("Mars", -1.524, 0, 0.533, Planet.RED, 6.42E23, 24077)
planets = [sun, mercury, venus, earth, mars]

#################  START FUNCTIONS  ###############
def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
        


#################   END FUNCTIONS   ###############

fps = 60
pygame.display.set_caption(
    f"{program_title}      fps - {fps}      by Abigail M. Lightle      Science Fair 2023-2024")

CLOCK = pygame.time.Clock()
ticks = 0
run = True
show_orbits = True
#################  START GAME LOOP  ###############
while run == True:
    CLOCK.tick(fps)
    ticks += 1

    # BLIT star background
    SCREEN.blit(img_background, (0, 0))
    
    # BLIT Text Rectangle (DISTANCE FROM SUN)
    pygame.draw.rect(SCREEN, Planet.GRAY, (30,120,290,220),
                     width = 0, border_radius = 20)
    pygame.draw.rect(SCREEN, Planet.WHITE, (30,120,290,220),
                     width = 3, border_radius = 20)    
    
    # BLIT Text Rectangle (SHORTCUTS)
    pygame.draw.rect(SCREEN, Planet.GRAY, (30,380,290,220),
                     width = 0, border_radius = 20)
    pygame.draw.rect(SCREEN, Planet.WHITE, (30,380,290,220),
                     width = 3, border_radius = 20)  
    
    # RECTANGLE (Law Of Gravitation)  
    pygame.draw.rect(SCREEN, Planet.GRAY, (30,640,290,220),
                     width = 0, border_radius = 20)
    pygame.draw.rect(SCREEN, Planet.WHITE, (30,640,290,220),
                     width = 3, border_radius = 20) 
    SCREEN.blit(img_newton, (35,685))   
    
    
    # BLIT Text to Screen
    SCREEN.blit(title_text, (225, 5))
    SCREEN.blit(abigail_text, (980, 840))
    SCREEN.blit(text_stats, (58,130))
    SCREEN.blit(text_shortcuts, (65,390))
    SCREEN.blit(text_gravity, (78,650))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause()
            if event.key == pygame.K_d:
                pass
            if event.key == pygame.K_o:
                show_orbits = not show_orbits

    # planets = [sun, mercury, venus, earth, mars]
    for planet in planets:
        planet.update_position(planets)
        planet.draw(SCREEN)
        if show_orbits:
            planet.draw_orbit(SCREEN)
      
    pygame.display.flip()

#################  END GAME LOOP ###############
pygame.quit()
