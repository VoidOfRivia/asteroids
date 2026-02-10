import pygame
import sys
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import player
import asteroid
import asteroidfield
import shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()
    dt = 0 

    # Creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Adding the Player class to the updatable and drawable groups
    player.Player.containers = (updatable, drawable)

    # Adding the Asteroids class to the asteroids group
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable,)
    
    # Adding the Shot class to the shots group
    shot.Shot.containers = (shots, updatable, drawable)

    # Spawning in the player
    spawn_player = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Spawning in the asteroids
    spawn_asteroids = asteroidfield.AsteroidField()

    # Infinite loop that runs the game after pygame has been called
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        updatable.update(dt)
        
        # Check for player-asteroid collisions
        for asteroid_obj in asteroids:
            if spawn_player.collides_with(asteroid_obj):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        # Check for shot-asteroid collisions
        for asteroid_obj in asteroids:
            for shot_obj in shots:
                if asteroid_obj.collides_with(shot_obj):
                    log_event("asteroid_shot")
                    asteroid_obj.split()  # Changed from .kill() to .split()
                    shot_obj.kill()
        
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()