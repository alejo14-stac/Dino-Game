import pygame
import random
import sys
import os

pygame.init()
WIDTH, HEIGHT = 900, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("dinosaurio GHRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
clock = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 24)

# Colors
BG_COLOR = (135, 206, 235)
BROWN = (120, 80, 40)
RED = (220, 60, 60)
WHITE = (255, 255, 255)

# Load sprites
dinosaurio_GHRRRRR = pygame.image.load(os.path.join("sprites", "dinosaurio_GHRRRRR.png")).convert_alpha()
dinosaurio_con_problemas_de_espalda = pygame.image.load(os.path.join("sprites", "dinosaurio_con_problemas_de_espalda.png")).convert_alpha()
loro_lucas. = pygame.image.load(os.path.join("sprites", "loro_lucas.png")).convert_alpha()
pincho_LAAAAARgo = pygame.image.load(os.path.join("sprites", "pincho_LAAAAARgo.png")).convert_alpha()
pincho = pygame.image.load(os.path.join("sprites", "pincho.png")).convert_alpha()

# scale sprites to expected sizes
dinosaurio_GHRRRRR = pygame.transform.scale(dinosaurio_GHRRRRR, (60, 80))
dinosaurio_con_problemas_de_espalda = pygame.transform.scale(dinosaurio_con_problemas_de_espalda, (60, 40))
pincho_LAAAAARgo = pygame.transform.scale(pincho_LAAAAARgo, (30, 60))
pincho = pygame.transform.scale(pincho, (40, 40))
loro_lucas = pygame.transform.scale(loro_lucas, (50, 30))

def run_game():
    # dino settings
    dino_img = dinosaurio_GHRRRRR
    dino = pygame.Rect(80, HEIGHT - 120, 60, 80)
    dino_vel_y = 0
    gravity = 0.5
    jump_strength = -15
    on_ground = True
    is_ducking = False

    # ground
    ground_y = HEIGHT - 40

    # obstacles and birds
    obstacles = []
    birds = []
    spawn_timer = 0
    spawn_delay = 90

