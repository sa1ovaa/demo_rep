import pygame
import random

# Инициализация
pygame.init()

# Экран
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# FPS
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Машина
car_width = 50
car_height = 100
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 10
car_speed = 5

# Coins
coin_size = 30
coins = []  # coin позициялары
coin_spawn_timer = 0

# Счет
score = 0
font = pygame.font.SysFont("Arial", 25)

# Главный цикл
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    # -------- EVENTS --------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -------- CONTROL --------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
        car_x += car_speed

    # -------- COINS SPAWN --------
    coin_spawn_timer += 1
    if coin_spawn_timer > 30:  # әр 0.5 секунд сайын coin
        x = random.randint(0, WIDTH - coin_size)
        coins.append([x, 0])
        coin_spawn_timer = 0

    # -------- COINS UPDATE --------
    for coin in coins:
        coin[1] += 5  # төмен түседі

    # -------- COLLISION --------
    for coin in coins[:]:
        coin_rect = pygame.Rect(coin[0], coin[1], coin_size, coin_size)
        car_rect = pygame.Rect(car_x, car_y, car_width, car_height)

        if coin_rect.colliderect(car_rect):
            coins.remove(coin)
            score += 1  # coin жинау

    # -------- DRAW CAR --------
    pygame.draw.rect(screen, BLACK, (car_x, car_y, car_width, car_height))

    # -------- DRAW COINS --------
    for coin in coins:
        pygame.draw.circle(screen, (255, 215, 0), (coin[0]+15, coin[1]+15), 15)

    # -------- DRAW SCORE --------
    text = font.render(f"Coins: {score}", True, BLACK)
    screen.blit(text, (WIDTH - 120, 10))  # жоғарғы оң жақ

    pygame.display.update()

pygame.quit()