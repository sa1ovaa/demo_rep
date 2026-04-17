import sys
import pygame
from ball import Ball

# Константы
WIDTH, HEIGHT = 600, 400
BACKGROUND_COLOR = (255, 255, 255)
FPS = 60

BALL_RADIUS = 25
BALL_COLOR = (255, 0, 0)
BALL_STEP = 20


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moving Ball Game")
    clock = pygame.time.Clock()

    # Создаем шар
    ball = Ball(
        x=WIDTH // 2,
        y=HEIGHT // 2,
        radius=BALL_RADIUS,
        color=BALL_COLOR
    )

    running = True

    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Движение строго по одному нажатию
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ball.move(0, -BALL_STEP, WIDTH, HEIGHT)
                elif event.key == pygame.K_DOWN:
                    ball.move(0, BALL_STEP, WIDTH, HEIGHT)
                elif event.key == pygame.K_LEFT:
                    ball.move(-BALL_STEP, 0, WIDTH, HEIGHT)
                elif event.key == pygame.K_RIGHT:
                    ball.move(BALL_STEP, 0, WIDTH, HEIGHT)

        # Рендер
        screen.fill(BACKGROUND_COLOR)
        ball.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()