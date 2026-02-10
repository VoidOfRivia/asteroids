import circleshape
import constants 
import pygame
import shot

class Player(circleshape.CircleShape): 
    def __init__(self, x, y): 
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0  # Add cooldown timer starting at 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), constants.LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * constants.PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        """Create a new shot at the player's position moving in the direction they're facing."""
        # Check if cooldown allows shooting
        if self.shot_cooldown > 0:
            return  # Prevent shooting if cooldown is active
        
        # Reset the cooldown timer
        self.shot_cooldown = constants.PLAYER_SHOOT_COOLDOWN_SECONDS
        
        # Create the shot
        new_shot = shot.Shot(self.position.x, self.position.y)
        
        # Calculate the shot's velocity
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        new_shot.velocity = direction * constants.PLAYER_SHOOT_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Decrease the cooldown timer every frame
        if self.shot_cooldown > 0:
            self.shot_cooldown -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()