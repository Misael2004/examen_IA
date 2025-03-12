import pygame
import os

# Inicializar pygame y el mezclador de sonido
pygame.init()
pygame.mixer.init()

# Configuración de pantalla
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prueba de Sonido")

# Cargar sonidos
if os.path.exists("jump.wav"):
    jump_sound = pygame.mixer.Sound("suspenso.mp3")
    jump_sound.set_volume(1.0)  # Asegurar volumen máximo
else:
    print("Error: No se encontró el archivo suspenso.mp3")

# Prueba de sonido
if 'jump_sound' in locals():
    print("Reproduciendo sonido...")
    jump_sound.play()
    pygame.time.delay(2000)  # Esperar 2 segundos para escuchar el sonido
else:
    print("No se puede reproducir el sonido. Verifica el archivo.")

# Salir de pygame
pygame.quit()
