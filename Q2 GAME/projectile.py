import pygame

class Projectile:
    def __init__(self, x, y, direction, speed=10):
        self.rect = pygame.Rect(x, y, 10, 5)  # Size of the projectile
        self.direction = direction  # -1 for left, 1 for right
        self.speed = speed

    def update(self, screen):
        self.rect.x += self.direction * self.speed  # Move the projectile in the specified direction
        pygame.draw.rect(screen, (255, 0, 0), self.rect)  # Draw the projectile on screen

    def check_collision(self, enemy):
        """Check if projectile hits an enemy."""
        if self.rect.colliderect(enemy.rect):
            enemy.health -= 10  # Reduce enemy's health
            return True  # Return True if collision happens
        return False
