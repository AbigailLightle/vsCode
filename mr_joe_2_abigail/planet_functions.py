import pygame
from planet_class import Planet
import planet_global_variables
import collections
import math


pygame.init()


def data(screen, clock, planets):
    clock.tick(60)
    show_data = True
    while show_data:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    show_data = False

        screen.fill('Purple')

        text_title = Planet.FONT_CS_36.render(
            f"Newtonian Orbital Simulation of the Terrestrial Planets\n\n           Revolutions per Earth Year", True, Planet.BLACK)
        text_abigail = Planet.FONT_CS_36.render(
            "by Abigail Lightle", True, Planet.WHITE)

        screen.blit(text_title, (200, 5))
        screen.blit(text_abigail, (1000, 845))

        planet_rev = Planet.earth_years_per_revolution(planets[1])
        planet_rec_text = Planet.FONT_CS_36.render(
            planet_rev[0] + "  " + str(planet_rev[1]), True, Planet.BLACK)
        screen.blit(planet_rec_text, (200, 250))

        planet_rev = Planet.earth_years_per_revolution(planets[2])
        planet_rec_text = Planet.FONT_CS_36.render(
            planet_rev[0] + "  " + str(planet_rev[1]), True, Planet.BLACK)
        screen.blit(planet_rec_text, (200, 350))

        planet_rev = Planet.earth_years_per_revolution(planets[3])
        planet_rec_text = Planet.FONT_CS_36.render(
            planet_rev[0] + "  " + str(planet_rev[1]), True, Planet.BLACK)
        screen.blit(planet_rec_text, (200, 450))

        planet_rev = Planet.earth_years_per_revolution(planets[4])
        planet_rec_text = Planet.FONT_CS_36.render(
            planet_rev[0] + "  " + str(planet_rev[1]), True, Planet.BLACK)
        screen.blit(planet_rec_text, (200, 550))

        img_excel_chart_01 = pygame.image.load(
            "Excel_Chart_01.png").convert_alpha()
        screen.blit(img_excel_chart_01, (25, 700))

        pygame.display.flip()


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False


def print_dts_min_avg_max(planets):
    for planet in planets:
        if planet != planets[0]:                     # != stands for not equal
            print(planet.name, len(planet.orbit))
            # print(planet.name)
            print("min", planet.dts_min)
            print("avg", planet.dts_avg)
            print('max', planet.dts_max)
            print('='*15)
        else:
            print()
            print()


def text_rectangle(screen, planets):
    # BLIT Text Rectangle (DISTANCE FROM SUN & TEXT)

    pygame.draw.rect(screen, Planet.GRAY, (30, 120, 290, 220),
                     width=0, border_radius=20)
    pygame.draw.rect(screen, Planet.WHITE, (30, 120, 290, 220),
                     width=3, border_radius=20)

    screen.blit(planet_global_variables.text_stats, (58, 130))

    if len(planets) > 4:
        planets[1].display_distance_to_sun(screen, 0, 95)
        planets[2].display_distance_to_sun(screen, 0, 138)
        planets[3].display_distance_to_sun(screen, 0, 181)
        planets[4].display_distance_to_sun(screen, 0, 223)


def text_shortcuts(screen):
    # BLIT Text Rectangle (SHORTCUTS & TEXT)
    pygame.draw.rect(screen, Planet.GRAY, (30, 365, 290, 250),
                     width=0, border_radius=20)
    pygame.draw.rect(screen, Planet.WHITE, (30, 365, 290, 250),
                     width=3, border_radius=20)

    screen.blit(planet_global_variables.text_shortcuts, (65, 375))

    screen.blit(planet_global_variables.text_arrow_up, (45, 415))
    screen.blit(planet_global_variables.text_arrow_down, (45, 443))
    screen.blit(planet_global_variables.text_pause, (45, 471))
    screen.blit(planet_global_variables.text_orbit, (45, 499))
    screen.blit(planet_global_variables.text_delete_sun, (45, 527))
    screen.blit(planet_global_variables.text_reset, (45, 555))
    screen.blit(planet_global_variables.text_venus, (45, 583))


def blit_title_and_name(screen):
    # BLIT Text to Screen
    screen.blit(planet_global_variables.title_text, (225, 5))
    screen.blit(planet_global_variables.abigail_text, (980, 840))


def sim_year_years_and_fps(screen, ticks, fps, program_title):
    # BLIT Simulated Earth Years and FPS
    text_earth_years = Planet.FONT_COURIER_22.render(
        f"sim-earth years: {ticks/365:.2f}", True, Planet.YELLOW)
    screen.blit(text_earth_years, (40, 55))

    # fps
    text_fps = Planet.FONT_COURIER_28.render(
        f"fps - {fps}", True, Planet.YELLOW)
    screen.blit(text_fps, (105, 80))

    # Caption
    pygame.display.set_caption(
        f"{program_title}      fps - {fps}      by Abigail M. Lightle      Science Fair 2023-2024")


def rectangle_law_of_gravity(screen, img):
   # RECTANGLE (Law Of Gravitation)
    pygame.draw.rect(screen, Planet.GRAY, (30, 640, 290, 220),
                     width=0, border_radius=20)
    pygame.draw.rect(screen, Planet.WHITE, (30, 640, 290, 220),
                     width=3, border_radius=20)

    screen.blit(planet_global_variables.text_gravity, (70, 650))

    screen.blit(img, (35, 685))
    screen.blit(planet_global_variables.text_scaled, (55, 872))


# def init_program_and_reset_variables(program_title):
#     global planets,sun,mercury,venus,earth,mars,fps,CLOCK,ticks,run,show_orbits

#     # Create Instances of Sun and Planets
#     # def __init__(self, name, x, y, relative_radius, color, mass, y_vel):

#     sun = Planet("Sun", 0, 0, 2.5, Planet.YELLOW,
#                     1.98892E30, 0)
#     mercury = Planet("Mercury", -0.387, 0, 0.376, Planet.DARK_GRAY,
#                         3.30e23, 47400)
#     venus = Planet("Venus", -0.723, 0, 0.949, Planet.WHITE,
#                     4.87E24, 35000)
#     earth = Planet("Earth", -1, 0, 1.0, Planet.BLUE,
#                     5.97E24, 29800)
#     mars = Planet("Mars", -1.524, 0, 0.533, Planet.RED,
#                     6.42E23, 24100)
#     planets = [sun, mercury, venus, earth, mars]

#     fps = 60
#     pygame.display.set_caption(
#         f"{program_title}      fps - {fps}      by Abigail M. Lightle      Science Fair 2023-2024")

#     CLOCK = pygame.time.Clock()
#     ticks = 0
#     run = True
#     show_orbits = True
