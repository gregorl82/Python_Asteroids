import pygame
import random

from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)


    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt


    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        random_angle = random.uniform(20.0, 50.0)
        first_asteroid_velocity = self.velocity.rotate(random_angle)
        second_asteroid_velcity = self.velocity.rotate(-(random_angle))

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid1.velocity = first_asteroid_velocity * 1.2
        asteroid2.velocity = second_asteroid_velcity * 1.2
