import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configurar la ventana
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Configurar el coche
CAR_WIDTH, CAR_HEIGHT = 50, 100
car = pygame.Rect(WIDTH // 2, HEIGHT // 2, CAR_WIDTH, CAR_HEIGHT)

# Configurar la velocidad del coche
SPEED = 5

# Configurar la carretera
ROAD_WIDTH = WIDTH
ROAD_HEIGHT = 100  # Hacer el rectángulo más grande
road = pygame.Rect(0, HEIGHT // 2, ROAD_WIDTH, ROAD_HEIGHT)

# Configurar los otros autos
OTHER_CARS = [pygame.Rect(random.randrange(WIDTH), random.randrange(HEIGHT), CAR_WIDTH, CAR_HEIGHT) for _ in range(5)]

# Configurar los power-ups
POWER_UPS = [pygame.Rect(random.randrange(WIDTH), random.randrange(HEIGHT), CAR_WIDTH, CAR_HEIGHT) for _ in range(3)]

# Configurar el contador de puntos
points = 90

# Configurar el sistema de puntuación
score = 0

# Configurar la fuente para mostrar el texto en la pantalla
font = pygame.font.Font(None, 36)

def draw_window():
    win.fill((0, 0, 0))  # Rellenar la ventana de negro
    pygame.draw.rect(win, (100, 100, 100), road)  # Dibujar la carretera
    pygame.draw.rect(win, (255, 0, 0), car)  # Dibujar el coche
    for other_car in OTHER_CARS:
        pygame.draw.rect(win, (0, 255, 0), other_car)  # Dibujar los otros autos
    for power_up in POWER_UPS:
        pygame.draw.rect(win, (0, 0, 255), power_up)  # Dibujar los power-ups

    # Dibujar la puntuación y los puntos restantes en la esquina superior izquierda
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    points_text = font.render(f"remaining points: {points}", True, (255, 255, 255))
    win.blit(score_text, (10, 10))
    win.blit(points_text, (10, 50))

    pygame.display.update()  # Actualizar la pantalla

def main():
    global points, score
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)  # Limitar el juego a 60 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and car.y - SPEED > 0:
            car.y -= SPEED
        if keys[pygame.K_DOWN] and car.y + SPEED < HEIGHT - CAR_HEIGHT:
            car.y += SPEED
        if keys[pygame.K_LEFT] and car.x - SPEED > 0:
            car.x -= SPEED
        if keys[pygame.K_RIGHT] and car.x + SPEED < WIDTH - CAR_WIDTH:
            car.x += SPEED

        # Mover los otros autos
        for other_car in OTHER_CARS:
            other_car.y += SPEED
            if other_car.y > HEIGHT:
                other_car.y = 0
                other_car.x = random.randrange(WIDTH)

        # Comprobar si el coche choca con otro auto
        for other_car in OTHER_CARS:
            if car.colliderect(other_car):
                points -= 1
                print(f"Puntos: {points}")
                if points <= 0:
                    print("¡Has perdido!")
                    pygame.quit()
                    sys.exit()

        # Comprobar si el coche recoge un power-up
        for power_up in POWER_UPS:
            if car.colliderect(power_up):
                score += 10
                print(f"Score: {score}")
                power_up.x = random.randrange(WIDTH)
                power_up.y = random.randrange(HEIGHT)

        # Si el coche sale de la ventana, cerrar el juego
        if car.x < 0 or car.x > WIDTH - CAR_WIDTH or car.y < 0 or car.y > HEIGHT - CAR_HEIGHT:
            pygame.quit()
            sys.exit()

        draw_window()

if __name__ == "__main__":
    main()
