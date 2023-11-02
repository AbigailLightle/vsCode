import pygame

import os
import math
from planet_class import Planet
import collections
import planet_functions
# import planet_global_variables

os.system('cls')

pygame.init()

WIDTH, HEIGHT = (1300, 900)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
Planet.WIDTH = WIDTH
Planet.HEIGHT = HEIGHT

program_title = "Newtonian Orbital Simulation of the Terrestrial Planets"

# create images (background with stars)
img_background = pygame.image.load("stars.jpg").convert()
img_newton = pygame.image.load("Newtons_Gravity_Law.png").convert_alpha()


def init_program_and_reset_variables():
    global planets, sun, mercury, venus, earth, mars, fps, CLOCK, ticks, run, show_orbits

    # Create Instances of Sun and Planets
    # def __init__(self, name, x, y, relative_radius, color, mass, y_vel):

    sun = Planet("Sun", 0, 0, 2.5, Planet.YELLOW,
                 1.98892E30, 0)
    mercury = Planet("Mercury", -0.387, 0, 0.376, Planet.DARK_GRAY,
                     3.30e23, 47400)
    venus = Planet("Venus", -0.723, 0, 0.949, Planet.WHITE,
                   4.87E24, 35000)
    earth = Planet("Earth", -1, 0, 1.0, Planet.BLUE,
                   5.97E24, 29800)
    mars = Planet("Mars", -1.524, 0, 0.533, Planet.RED,
                  6.42E23, 24100)
    planets = [sun, mercury, venus, earth, mars]

    fps = 60
    pygame.display.set_caption(
        f"{program_title}      fps - {fps}      by Abigail M. Lightle      Science Fair 2023-2024")

    CLOCK = pygame.time.Clock()
    ticks = 0
    run = True
    show_orbits = True


init_program_and_reset_variables()

#################  START GAME LOOP  ###############
while run == True:
    CLOCK.tick(fps)
    ticks += 1

    # BLIT star background
    SCREEN.blit(img_background, (0, 0))

    # BLIT Text Rectangle (DISTANCE FROM SUN & TEXT)
    planet_functions.text_rectangle(SCREEN, planets)

    # BLIT Text Rectangle (SHORTCUTS & TEXT)
    planet_functions.text_shortcuts(SCREEN)

    # blit Image Rectangle (Law Of Gravitation)
    planet_functions.rectangle_law_of_gravity(SCREEN, img_newton)

    # BLIT Title and Nam to Screen
    planet_functions.blit_title_and_name(SCREEN)

    # BLIT Simulated Earth Years. FPS, and Caption
    planet_functions.sim_year_years_and_fps(SCREEN, ticks, fps, program_title)

    # Update and Draw planet positions
    # planets = [sun, mercury, venus, earth, mars]
    for planet in planets:
        planet.update_position(planets)
        planet.draw(SCREEN)
        if show_orbits:
            planet.draw_orbit(SCREEN)

    # Event Detection
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                planet_functions.pause()
            if event.key == pygame.K_DOWN:
                fps = (fps-5) if fps > 5 else fps
            if event.key == pygame.K_UP:
                fps += 5
            if event.key == pygame.K_o:
                for planet in planets:
                    planet.dts_sum_num = 0
                    planet.orbit = []
                    planet.orbit = collections.deque(
                        maxlen=math.ceil(planet.orbital_period))
                    planet.orbit.clear()
                    planet.orbit.append((planet.x, planet.y))
                show_orbits = not show_orbits
            if event.key == pygame.K_s:
                planets.remove(sun)
            if event.key == pygame.K_r:
                del sun
                del mercury
                del venus
                del earth
                del mars
                init_program_and_reset_variables()
            if event.key == pygame.K_x:
                for planet in planets:
                    if planet.name != "Sun":
                        print(
                            f"*** {planet.name} {planet.dts_sum_num} {len(planet.orbit)} ***")
                        print(planet.dts_min)
                        print(planet.dts_avg)
                        print(planet.dts_max)
                        print()
            if event.key == pygame.K_d:
                planet_functions.data(SCREEN, CLOCK, planets)
            if event.key == pygame.K_m:
                planet_functions.print_dts_min_avg_max(planets)
            if event.key == pygame.K_v:
                venus.y_vel *= 1.07
                venus.x_vel *= 1.07

                
    pygame.display.flip()

#################  END GAME LOOP ###############

pygame.quit()
