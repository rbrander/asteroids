import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
  print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()

  Asteroid.containers = (asteroids, updatable, drawable)

  AsteroidField.containers = (updatable)
  asteroidField = AsteroidField()

  Player.containers = (updatable, drawable)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  dt = 0

  # Game loop
  while True:
    log_state()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    # update
    updatable.update(dt)

    # draw
    screen.fill("black")
    for obj in drawable:
      obj.draw(screen)
    pygame.display.flip()

    # wait for next frame
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()
