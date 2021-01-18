import pygame
import Enemies

minion1 = Enemies.minion_make()

white = (255, 255, 255)

"""For variable descriptions, see def wall_make"""


class Wall(pygame.sprite.Sprite):
    def __init__(self):
        """ Wall constructor class for all walls be placed in various areas of a level"""
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = None
        self.transport_to_screen = None
        self.transport_to_xy = None
        self.transport_x_or_y = None
        self.items = None
        self.message = None
        self.enemy = None


class Screen():
    def __init__(self):
        self.objects = None  # a list of all the objects on a screen. three types, wall, item container, and doorway/
        self.background_img = None  # background image                                                transporting wall
        self.background_pos = None


class Level():
    """ This is a generic super-class used to define a level."""

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    def __init__(self):
        self.screen_list = []
        self.current_screen = 0


"""image is a list containing either a true or false statement as the first item and a second item that is either
an image, or another false statement. The first boolean determines whether or not an image is included when 
the function is called

rect is a list that helps created the rectangle when the wall surface is created. the first item corresponds to the
left side of the rectangle, the second corresponds to the top, the third the right side, and the last to the bottom.
These allow the function to place the rectangle on the screen. If a side is not needed, it is left false

The transport to screen variable states the screen that the wall transports you to (left as False if just a regular
wall). The next variables determine what x or y value to set the player to if they cross the wall and the x or y 
variable states which coordinate variable (x or y) to keep the same

the items variable is a multidimensional list (left as False if empty) that contains the items that the wall will 
contain 
[[item name, [attribute item affects, value], item image, item description]] 
(the outer brackets are there in case there is more than one item per wall)

There are four types: wall, container, enemy, and message
container and message display a message when the space bar is pressed based on the item or message associated with each 
respectively
"""


def wall_make(image, rect, transport_to_screen, transport_to_xy, transport_x_or_y, items, message, enemy):
    wall = Wall()
    if image[0]:
        wall.image = image[1]
    else:
        wall.image = pygame.Surface(image[1])
        wall.image.fill((0, 0, 0))
    wall.rect = wall.image.get_rect()
    if rect[0]:
        wall.rect.left = rect[0]
    if rect[1]:
        wall.rect.top = rect[1]
    if rect[2]:
        wall.rect.right = rect[2]
    if rect[3]:
        wall.rect.bottom = rect[3]
    if transport_to_screen is not False:
        wall.transport_to_screen = transport_to_screen
        wall.transport_to_xy = transport_to_xy
        wall.transport_x_or_y = transport_x_or_y
    if items:
        wall.items = items
    if message:
        wall.message = message
    if enemy:
        wall.enemy = enemy
    return wall


"""LEVEL 1"""

Level_1 = Level()

"""SCREEN 1 LEVEL 1"""

screen1_level1_background = pygame.image.load("p_main.jpg")
# screen1_level1_background.fill(white)

screen1_level1 = Screen()
walls = pygame.sprite.Group()
wall = wall_make([False, [10, 600]], [-10, 0, False, False], 3, 715, "y", False, False, False)
walls.add(wall)
# left barrier

wall = wall_make([False, [800, 10]], [0, -10, False, False], 4, 515, "x", False, False, False)
walls.add(wall)
# top barrier

wall = wall_make([False, [800, 10]], [0, 600, False, False], 2, 0, "x", False, False, False)
walls.add(wall)
# bottom barrier

wall = wall_make([False, [10, 600]], [800, 0, False, False], 1, 0, "y", False, False, False)
walls.add(wall)
# right barrier

screen1_level1.objects = walls
screen1_level1.background_img = screen1_level1_background
screen1_level1.background_pos = (0, 0)

"""SCREEN 2 LEVEL 1"""

screen2_level1_background = pygame.image.load("p_right.jpg")

screen2_level1 = Screen()
walls = pygame.sprite.Group()
wall = wall_make([False, [800, 10]], [0, 600, False, False], False, False, False, False, False, False)
walls.add(wall)
# bottom barrier

wall = wall_make([False, [10, 600]], [-10, 0, False, False], 0, 715, "y", False, False, False)
walls.add(wall)
# left barrier

enemy = wall_make([True, Enemies.pboss_sprite], [400, 300, False, False], False, False, False, False, False, "p_boss")
walls.add(enemy)
# enemy (cat)

screen2_level1.objects = walls
screen2_level1.background_img = screen2_level1_background
screen2_level1.background_pos = (0, 0)

"""SCREEN 3 LEVEL 1"""

screen3_level1_background = pygame.image.load("p_down.jpg")

screen3_level1 = Screen()
walls = pygame.sprite.Group()
wall = wall_make([False, [800, 10]], [0, 600, False, False], False, False, False, False, False, False)
walls.add(wall)
# bottom barrier

wall = wall_make([False, [10, 600]], [-10, 0, False, False], False, False, False, False, False, False)
walls.add(wall)
# left barrier

wall = wall_make([False, [800, 10]], [0, -10, False, False], 0, 515, "x", False, False, False)
walls.add(wall)
# top barrier

wall = wall_make([False, [10, 600]], [800, 0, False, False], False, False, False, False, False, False)
walls.add(wall)
# right barrier

screen3_level1.objects = walls
screen3_level1.background_img = screen3_level1_background
screen3_level1.background_pos = (0, 0)

"""SCREEN 4 LEVEL 1"""

screen4_level1_background = pygame.image.load("p_left.jpg")

screen4_level1 = Screen()
walls = pygame.sprite.Group()
wall = wall_make([False, [800, 10]], [0, 600, False, False], False, False, False, False, False, False)
walls.add(wall)
# bottom barrier

wall = wall_make([False, [10, 600]], [-10, 0, False, False], False, False, False, False, False, False)
walls.add(wall)
# left barrier

wall = wall_make([False, [800, 10]], [0, -10, False, False], False, False, False, False, False, False)
walls.add(wall)
# top barrier

wall = wall_make([False, [10, 600]], [800, 0, False, False], 0, 0, "y", False, False, False)
walls.add(wall)
# right barrier

screen4_level1.objects = walls
screen4_level1.background_img = screen4_level1_background
screen4_level1.background_pos = (0, 0)

"""SCREEN 5 LEVEL 1"""

screen5_level1_background = pygame.image.load("p_up.jpg")

screen5_level1 = Screen()
walls = pygame.sprite.Group()
wall = wall_make([False, [800, 10]], [0, 600, False, False], 0, 0, False, False, False, False)
walls.add(wall)
# bottom barrier

wall = wall_make([False, [10, 600]], [-10, 0, False, False], False, False, False, False, False, False)
walls.add(wall)
# left barrier

wall = wall_make([False, [800, 10]], [0, -10, False, False], False, False, False, False, False, False)
walls.add(wall)
# top barrier

wall = wall_make([False, [10, 600]], [800, 0, False, False], False, False, False, False, False, False)
walls.add(wall)
# right barrier

screen5_level1.objects = walls
screen5_level1.background_img = screen5_level1_background
screen5_level1.background_pos = (0, 0)

Level_1.screen_list.append(screen1_level1)
Level_1.screen_list.append(screen2_level1)
Level_1.screen_list.append(screen3_level1)
Level_1.screen_list.append(screen4_level1)
Level_1.screen_list.append(screen5_level1)
