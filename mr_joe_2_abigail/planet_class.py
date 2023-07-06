import pygame
import math
import collections

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
    MASS_OF_SUN = 1.98892E30
    WIDTH = None
    HEIGHT = None
    MAX_ORBIT_LENGTH = 1000  # trial and error

    # create COLORS
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    BLUE = (100, 149, 237)
    RED = (188, 39, 50)
    GRAY = (128, 128, 128)
    DARK_GRAY = (80, 78, 81)
    BLACK = (0, 0, 0)

    # create FONTS
    FONT_COURIER_16 = pygame.font.SysFont(
        "Courier", 16, bold=True)
    FONT_COURIER_18 = pygame.font.SysFont("Courier", 18)
    FONT_COURIER_20 = pygame.font.SysFont("Courier", 20, bold=True)
    FONT_COURIER_22 = pygame.font.SysFont("Courier", 22, bold=True)
    FONT_COURIER_28 = pygame.font.SysFont("Courier", 28, bold=True)
    FONT_COURIER_32 = pygame.font.SysFont("Courier", 32)
    FONT_CS_36 = pygame.font.SysFont("comicsans", 36)

    def __init__(self, name, x, y, relative_radius, color, mass, y_vel):
        self.name = name
        self.x = x * Planet.AU
        self.y = y * Planet.AU

        self.radius = relative_radius * Planet.EARTH_SIZE
        self.color = color

        self.mass = mass

        self.distance_to_sun = math.sqrt(self.x**2 + self.y**2)

        self.orbital_period = math.sqrt(
            (4*math.pi**2 * (self.distance_to_sun)**3) / (Planet.G * Planet.MASS_OF_SUN))/(60*60*24)
        # print(self.name,self.orbital_period)

        # self.orbit = [(self.x, self.y)]
        self.orbit = collections.deque(
            maxlen=math.ceil(int(self.orbital_period)))
        # self.orbit.clear()
        self.orbit.append((self.x, self.y))

        self.dts_min = 9999999999999  # minimum initial st HIGH
        self.dts_max = 0
        self.dts_sum = 0
        self.dts_sum_num = 0
        self.dts_avg = 0

        self.x_vel = 0
        self.y_vel = y_vel

    def earth_years_per_revolution(self):
        return self.name, self.orbital_period
        # self.time_per_revolution = abs(
        #     1/(self.x/Planet.AU/self.y_vel*Planet.EARTH_VELOCITY))
        # return self.name, self.time_per_revolution

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        # F = MA    A = (F/M)      Vel = A * Time
        self.x_vel += (total_fx / self.mass) * self.TIMESTEP
        self.y_vel += (total_fy / self.mass) * self.TIMESTEP

        # Distance = Vel * Time     (new location)
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP

        self.orbit.append((self.x, self.y))     # save new location for orbit

        dts = math.sqrt(self.x**2 + self.y**2)
        self.dts_sum_num += 1
        self.dts_min = int(dts if dts < self.dts_min else self.dts_min)
        self.dts_max = int(dts if dts > self.dts_max else self.dts_max)
        self.dts_sum += dts
        self.dts_avg = int(self.dts_sum / self.dts_sum_num)

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
        x = (self.x * Planet.SIZE_SCALE) + \
            Planet.WIDTH/2 + Planet.CENTER_OFFSET_X
        y = (self.y * Planet.SIZE_SCALE) + \
            Planet.HEIGHT/2 + Planet.CENTER_OFFSET_Y
        pygame.draw.circle(win, self.color, (x, y), self.radius)

        # Place names on Planets & Sun
        planet_text = Planet.FONT_COURIER_16.render(self.name, 1, Planet.WHITE)
        below = 1.25 if self.name == "Sun" else 2.0
        win.blit(planet_text, (x - planet_text.get_width()/2,
                               y - planet_text.get_height()/2 + below * self.radius))

    def draw_orbit(self, win):
        updated_points = []
        for point in self.orbit:
            x, y = point
            x = (x * Planet.SIZE_SCALE + Planet.WIDTH / 2) + \
                Planet.CENTER_OFFSET_X
            y = (y * Planet.SIZE_SCALE + Planet.HEIGHT / 2) + \
                Planet.CENTER_OFFSET_Y
            updated_points.append((x, y))

        if len(updated_points) > 1:
            pygame.draw.lines(win, self.color, False, updated_points, 2)

    def display_distance_to_sun(self, win, x, y):
        pygame.draw.circle(win, self.color, (60 + x, 88+y), self.radius)

        if self.name == "Mercury":
            distance_text = Planet.FONT_COURIER_16.render(
                f"{self.name}  {math.floor(self.distance_to_sun/1000)} km", True, Planet.BLACK)
        if self.name == "Venus":
            distance_text = Planet.FONT_COURIER_16.render(
                f"{self.name}   {math.floor(self.distance_to_sun/1000)} km", True, Planet.BLACK)
        if self.name == "Earth":
            distance_text = Planet.FONT_COURIER_16.render(
                f"{self.name}   {math.floor(self.distance_to_sun/1000)} km", True, Planet.BLACK)
        if self.name == "Mars":
            distance_text = Planet.FONT_COURIER_16.render(
                f"{self.name}    {math.floor(self.distance_to_sun/1000)} km", True, Planet.BLACK)

        win.blit(distance_text, (x + 100, 78 + y))
