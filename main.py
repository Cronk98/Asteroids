# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroids import *
from asteroidfield import *
from circleshape import *


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\n"
          f"Screen height: {SCREEN_HEIGHT}"
          )
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill(000)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collision(player) == True:
                print("Game over!")
                exit()
        
        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid) == True:
                    asteroid.kill()
                    shot.kill()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
