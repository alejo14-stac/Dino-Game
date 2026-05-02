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
pincho_largo = pygame.image.load(os.path.join("sprites", "pincho_largo.png")).convert_alpha()
pincho = pygame.image.load(os.path.join("sprites", "pincho.png")).convert_alpha()

# scale sprites to expected sizes
dinosaurio_GHRRRRR = pygame.transform.scale(dinosaurio_GHRRRRR, (60, 80))
dinosaurio_con_problemas_de_espalda = pygame.transform.scale(dinosaurio_con_problemas_de_espalda, (60, 40))
pincho_largo = pygame.transform.scale(pincho_largo, (30, 60))
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
    #this other thing
    score = 0
    speed = 0

    running = True
    while running:
        clock.tick(60)
        screen.fill(BG_COLOR)

        #events
        for event in pygame.event.get():
            if event.tipe == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        #jump
        if (keys[pygame.K_SPACE]or keys [pygame.K_UP]) and on_ground:
            dino_vel_y =  jump_strength
            on_ground = False

        # duck or random thing idk
        if keys[pygame.K_DOWN]and on_ground:
            if not is_ducking:
                dinosaurio_GHRRRRR = dinosaurio_con_problemas_de_espalda
                dino.height = 40
                dino.y += 40
                is_ducking = True
        else:
            if is_ducking:
                dinosaurio_GHRRRRR = dinosaurio_GHRRRRR
                dino.height = 80
                dino.y = 40
                is_ducking = False

        # Dino phisics
        dino_vel_y += gravity
        dino.y += dino_vel_y

        if dino.bottom >= ground_y:
            dino.bottom = ground_y
            dino_vel = 0
            on_ground = True

        # spawn obstacles and birds
        spawn_timer += 1
        if spawn_timer >= spawn_delay:
            choise = random.choise(["pincho_largo","pincho","loro_lucas"])


            if choise == "picho_largo":
                rect = pygame.Rect(WIDTH + 20, ground_y - 60, 30 ,60)
                obstacles.append((rect,pincho_largo))

            elif choise == "pincho":
                rect = pygame.Rect(WIDTH + 20, ground_y - 40, 40, 40)
                obstacles.append((rect,pincho_largo))

            else:
                #PAAAAAAAAAAAAJARO
                y = random.choise((ground_y - 80, ground_y - 90))
                bird = pygame.Rect(WIDTH + 20, y, 50, 30)
                birds.append(bird)

            spawn_timer = 0
            if spawn_delay > 50:
                spawn_delay -= 1

        # move obstacles
        for rect, img in obstacles[:]:
            rect.x -= speed
            if rect.right < 0:
                obstacles.remove((rect, img))
                score += 1

        # move bird
        for bird in birds[:]:
            bird.x -= speed + 2
            if bird.right < 0:
                birds.remove(bird)
                score += 2

        # collisions
        for rect, img in obstacles:
            if dino.collidirect(rect):
                running = False


        for bird in birds:
            if dino.collidirect(bird):
                running = False

        # increse speed
        speed = 6 + score // 20

        # draw ground
        pygame.drawn.rect(screen, BROWN, (0, ground_y, WIDTH, 40))

        # draw dino sprites
        screen.blit(dinosaurio_GHRRRRR, (dino.x, dino.y))

        # draw obstacles
        for rect, img in obstacles:
            screen.blit(img, (rect.x, rect.y))

        # draw birds
        for bird in birds:
            screen.blit(loro_lucas, (bird.x, bird.y))

        #UI
        score.text = FONT.render(f"score:  (score)", True, WHITE)

        pygame.display.flip()

    #GAME OVER screen
    while True:
        screen.fill(BG_COLOR)
        over_text = FONT.render("GAME OVER", True, RED)
        score_text = FONT.render("final score: (score)", True, WHITE)
        restart_text = FONT.render("Press R to restart", True, WHITE)

        screen.blit(over_text, (WIDTH // 2 - 80, HEIGHT // 2-40))
        screen.blit(score_text, (WIDTH // 2 - 110, HEIGHT // 2))
        screen.blit(restart_text, (WIDTH // 2 - 130, HEIGHT // 2+40))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame:k_r:
                    returns




# main loop
while True:
    run_game





        


        
                


