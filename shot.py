import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def update(self, dt: float):
        self.position += self.velocity * dt
    def draw(self, screen: pygame.Surface):
        color = "white"
        position = self.position
        radius = self.radius
        width = LINE_WIDTH
        pygame.draw.circle(screen, color, position, radius, width)
