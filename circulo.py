import pygame
import sys

# Dimensiones de la ventana
WIDTH = 800
HEIGHT = 600

# Colores
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Inicializar Pygame
pygame.init()

# Crear la ventana
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Círculo rebotando")

# Posición y velocidad inicial del círculo
x = 50
y = 50
vel_x = 5
vel_y = 5
radius = 30

clock = pygame.time.Clock()

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mover el círculo
    x += vel_x
    y += vel_y

    # Comprobar colisión con los bordes de la ventana
    if x + radius > WIDTH or x - radius < 0:
        vel_x = -vel_x
    if y + radius > HEIGHT or y - radius < 0:
        vel_y = -vel_y

    # Pintar el fondo de negro
    window.fill(BLACK)

    # Dibujar el círculo
    pygame.draw.circle(window, RED, (x, y), radius)

    # Actualizar la ventana
    pygame.display.flip()

    # Controlar la velocidad de fotogramas
    clock.tick(60)
