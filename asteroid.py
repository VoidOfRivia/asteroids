import circleshape
import constants
import pygame
import random  # Add this import
from logger import log_event  # Add this import

class Asteroid(circleshape.CircleShape): 
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Overriding the draw class in the circleshape.py    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH) 

    # Overriding the update class in the circleshape.py
    def update(self, dt): 
        self.position += (self.velocity * dt)
    
    def split(self):
        """Split the asteroid into two smaller asteroids, or destroy if already small."""
        # Always kill this asteroid first
        self.kill()
        
        # If this is a small asteroid, just return (it's destroyed)
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        # Otherwise, spawn 2 new smaller asteroids
        log_event("asteroid_split")
        
        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)
        
        # Create two new velocity vectors by rotating the current velocity
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        
        # Calculate the new smaller radius
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        
        # Create the first new asteroid
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1 * 1.2  # Make it move 20% faster
        
        # Create the second new asteroid
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2 * 1.2  # Make it move 20% faster