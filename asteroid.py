import circleshape
import constants 
import pygame

class Asteroid(circleshape.CircleShape): 
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    #overriding the draw class in the  circleshape.py    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH) 

    #overriding the update class in the  circleshape.py
    def update(self,dt): 
        self.position += (self.velocity * dt)