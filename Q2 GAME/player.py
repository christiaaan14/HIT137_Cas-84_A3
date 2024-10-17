import pygame
from projectile import Projectile

class Player:
    def __init__(self, x, y, image):
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.jump = False
        self.jump_vel = -15
        self.gravity = 0.8
        self.health = 100
        self.lives = 3
        self.y_vel = 0
        self.projectiles = []

    def update(self, screen):
        keys = pygame.key.get_pressed()

        # Player Movement
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if not self.jump:
            if keys[pygame.K_SPACE]:
                self.jump = True
                self.y_vel = self.jump_vel
        if self.jump:
            self.rect.y += self.y_vel
            self.y_vel += self.gravity
            if self.rect.y >= 550:
                self.rect.y = 550
                self.jump = False

        # Handle projectiles
        for projectile in self.projectiles:
            projectile.update(screen)
            # You can check for collisions here

        # Player shooting
        if keys[pygame.K_f]:  # 'F' to fire
            self.shoot()

        # Draw player
        screen.blit(self.image, self.rect.topleft)

    def shoot(self):
        direction = 1 if self.rect.x > 0 else -1  # Shoot right if facing right
        projectile = Projectile(self.rect.x, self.rect.y + 25, direction)
        self.projectiles.append(projectile)
