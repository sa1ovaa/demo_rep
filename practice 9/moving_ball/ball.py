
import pygame

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def move(self, dx, dy, screen_width, screen_height):
        # новая позиция
        new_x = self.x + dx
        new_y = self.y + dy

        # проверка границ (чтобы не выходил за экран)
        if self.radius <= new_x <= screen_width - self.radius:
            self.x = new_x

        if self.radius <= new_y <= screen_height - self.radius:
            self.y = new_y

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)