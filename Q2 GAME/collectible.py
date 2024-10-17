import pygame

class Collectible:
    def __init__(self, x, y, image):
        self.image = pygame.transform.scale(image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collected = False

    def update(self, screen, player):
        if self.rect.colliderect(player.rect):
            self.collected = True
            player.health += 10  # Give the player a health boost or other benefit
        if not self.collected:
            screen.blit(self.image, self.rect.topleft)
