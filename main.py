import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()
    dt = 0 

    #creating two empty groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #adding the Player class to the udpateable and drawable groups
    player.Player.containers = (updatable, drawable)

    #spawning in the player
    spawn_player = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #infinte loop that runs the game after pygame has been called
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")
        updatable.update(dt)
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
