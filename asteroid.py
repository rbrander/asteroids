import random
from circleshape import CircleShape
from constants import ASTEROID_LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame

from logger import log_event


class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, ASTEROID_LINE_WIDTH)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    log_event("asteroid_split")
    randomAngle = random.uniform(20, 50)
    newVelocity = self.velocity * 1.2
    newRadius = self.radius - ASTEROID_MIN_RADIUS
    leftAsteroid = Asteroid(self.position.x, self.position.y, newRadius)
    leftAsteroid.velocity = newVelocity.rotate(-randomAngle)
    rightAsteroid = Asteroid(self.position.x, self.position.y, newRadius)
    rightAsteroid.velocity = newVelocity.rotate(randomAngle)

