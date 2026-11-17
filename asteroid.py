import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        color = "white"
        position = self.position
        radius = self.radius
        width = LINE_WIDTH
        pygame.draw.circle(screen, color, position, radius, width)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <=ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        newangle = random.uniform(20, 50)
        vel1 = self.velocity.rotate(newangle)
        vel2 = self.velocity.rotate(-newangle)
        newradius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, newradius)
        asteroid2 = Asteroid(self.position.x, self.position.y, newradius)
        asteroid1.velocity = vel1 * 1.2
        asteroid2.velocity = vel2 * 1.2
