import pygame
import random
import os
import sys
import puntuacion

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jump King Infinite")

# Colores
BLUE = (135, 206, 250)
BROWN = (139, 69, 19)
RED = (255, 0, 0)

# Cargar sprite del jugador
sprite_path = os.path.join("kate.png")
player_sprite = pygame.image.load(sprite_path)
player_sprite = pygame.transform.scale(player_sprite, (30, 30))

# Jugador
player = pygame.Rect(200, 500, 30, 30)
velocity_y = 0
velocity_x = 0
speed = 5
gravity = 0.5
jump_strength = -10
jumping = False

# Plataformas
platforms = [pygame.Rect(random.randint(50, 300), HEIGHT - i * 100, 100, 10) for i in range(7)]

clock = pygame.time.Clock()
run = True
score = 0

while run:
    screen.fill(BLUE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                velocity_y = jump_strength
                jumping = True
            if event.key == pygame.K_LEFT:
                velocity_x = -speed
            if event.key == pygame.K_RIGHT:
                velocity_x = speed
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                velocity_x = 0
    
    # Aplicar gravedad
    velocity_y += gravity
    player.y += velocity_y
    player.x += velocity_x
    
    # Mantener al jugador dentro de la pantalla
    if player.x < 0:
        player.x = 0
    if player.x + player.width > WIDTH:
        player.x = WIDTH - player.width
    
    # Desplazamiento de pantalla
    if player.y < HEIGHT // 2:
        for platform in platforms:
            platform.y += abs(velocity_y)
        score += 1
    
    # Colisión con plataformas y generación infinita
    new_platforms = []
    for platform in platforms:
        pygame.draw.rect(screen, BROWN, platform)
        if player.colliderect(platform) and velocity_y > 0:
            player.y = platform.y - player.height
            velocity_y = 0
            jumping = False
        if platform.y < HEIGHT:
            new_platforms.append(platform)
    
    while len(new_platforms) < 7:
        new_platforms.append(pygame.Rect(random.randint(50, 300), new_platforms[-1].y - 100, 100, 10))
    
    platforms = new_platforms
    
    # Dibujar jugador con sprite
    screen.blit(player_sprite, (player.x, player.y))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
