import pygame
from planet_class import Planet


# create TEXT for visible SCREEN output
# create_text_for_screen_output()
program_title = "Newtonian Orbital Simulation of the Terrestrial Planets"

title_text = Planet.FONT_CS_36.render(
    "Newtonian Orbital Simulation of the Terrestrial Planets",
    True, Planet.WHITE)

abigail_text = Planet.FONT_CS_36.render("By: Abigail Lightle", True, Planet.WHITE)
text_stats = Planet.FONT_COURIER_20.render("Distance from the Sun", True, Planet.BLACK)
text_gravity = Planet.FONT_COURIER_20.render("Law of Gravitation", True, Planet.BLACK)
text_shortcuts = Planet.FONT_COURIER_20.render("Keyboard Shortcuts", True, Planet.BLACK)
text_arrow_up = Planet.FONT_COURIER_16.render("Up Arrow   - FPS up 5", True, Planet.BLACK)
text_arrow_down = Planet.FONT_COURIER_16.render("Down Arrow - FPS down 5", True, Planet.BLACK)
text_pause = Planet.FONT_COURIER_16.render("p          - Pause Toggle", True, Planet.BLACK)
text_orbit = Planet.FONT_COURIER_16.render("o          - Orbit Toggle", True, Planet.BLACK)
text_delete_sun = Planet.FONT_COURIER_16.render("s          - Delete Sun", True, Planet.BLACK)
text_reset = Planet.FONT_COURIER_16.render("r          - Reset", True, Planet.BLACK)
text_venus = Planet.FONT_COURIER_16.render("v          - Inc Venus Vel", True, Planet.BLACK)

text_scaled = Planet.FONT_COURIER_18.render(
    "All variables scaled accurately except visual size of the Sun and Planets ...",
    True, Planet.YELLOW)



