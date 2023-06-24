import pygame
import math

pygame.init()

class Planet():
    # class constants
    AU = 149.5978707E9   # meters
    G = 6.6743E-11
    SIZE_SCALE = 250/AU     # 250 pixels per AU
    TIMESTEP = 60*60*24    # 1 day in secs
    CENTER_OFFSET_X = 175
    CENTER_OFFSET_Y = 0 
    EARTH_SIZE = 20    # Relative Radius
    EARTH_VELOCITY = 29783
    WIDTH = None
    HEIGHT = None 
    STOP_AFTER = 1000  # trial and error
    
    # create COLORS
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    BLUE = (100, 149, 237)
    RED = (188, 39, 50)
    GRAY = (128, 128, 128)
    DARK_GRAY = (80, 78, 81)
    BLACK = (0, 0, 0)    
    
    # create FONTS
    FONT_LST_16 = pygame.font.SysFont("Lucida Sans Typewriter", 16)
    FONT_LST_18 = pygame.font.SysFont("Lucida Sans Typewriter", 18)
    FONT_LST_20 = pygame.font.SysFont("Lucida Sans Typewriter", 20)
    FONT_LST_22 = pygame.font.SysFont("Lucida Sans Typewriter", 22)
    FONT_LST_28 = pygame.font.SysFont("Lucida Sans Typewriter", 28)
    FONT_LST_32 = pygame.font.SysFont("Lucida Sans Typewriter", 32)
    FONT_CS_36 = pygame.font.SysFont("comicsans", 36)
    

    def __init__(self, name, x, y, relative_radius, color, mass, y_vel):
        self.name = name
        self.x = x * Planet.AU
        self.y = y * Planet.AU

        self.radius = relative_radius * Planet.EARTH_SIZE
        self.color = color

        self.mass = mass

        self.orbit = [(self.x, self.y)]
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = y_vel
     
     
    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP

        # (stop after STOP_AFTER points)
        if len(self.orbit) < Planet.STOP_AFTER:
            self.orbit.append((self.x, self.y))   
            
                 
    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.name == "Sun":
            self.distance_to_sun = distance

        force = Planet.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y
        

    def draw(self, win):
        
        # Planet.draw_orbit(self,win)
        
        x = (self.x * Planet.SIZE_SCALE) + Planet.WIDTH/2 + Planet.CENTER_OFFSET_X
        y = (self.y * Planet.SIZE_SCALE) + Planet.HEIGHT/2 + Planet.CENTER_OFFSET_Y
        pygame.draw.circle(win, self.color, (x, y), self.radius)
        
        # Place names on Planets & Sun
        planet_text = Planet.FONT_LST_16.render(self.name, 1, Planet.WHITE)
        below = 1.25 if self.name == "Sun" else 2.0
        win.blit(planet_text, (x - planet_text.get_width()/2,
                               y - planet_text.get_height()/2 + below * self.radius))
        
    def draw_orbit(self,win):
        # draw orbits (stop after STOP_AFTER points)
        # if len(self.orbit) > 1:
        updated_points = []
        for point in self.orbit:
            x, y = point
            x = (x * Planet.SIZE_SCALE + Planet.WIDTH / 2) + Planet.CENTER_OFFSET_X
            y = (y * Planet.SIZE_SCALE + Planet.HEIGHT / 2) + Planet.CENTER_OFFSET_Y

            if len(updated_points) < Planet.STOP_AFTER:
                updated_points.append((x, y))

        pygame.draw.lines(win, self.color, False, updated_points, 2)
