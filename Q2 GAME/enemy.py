import pygame

class Enemy:
    def __init__(self, x, y, image, is_boss=False):
        self.image = pygame.transform.scale(image, (100, 100) if is_boss else (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3 if is_boss else 3  # Adjusted speed for bosses
        self.health = 200 if is_boss else 50  # Boss has higher health to make it harder to kill
        self.is_boss = is_boss

    def update(self, screen, player=None):
        if player:
            self.follow_player(player)  # Follow the player's movement 100%

        # Draw the health bar and the enemy itself
        self.draw_health_bar(screen)
        screen.blit(self.image, self.rect.topleft)

    def follow_player(self, player):
        """Enemy follows the player's position."""
        # Move toward the player's horizontal position (x-axis)
        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
        elif self.rect.x > player.rect.x:
            self.rect.x -= self.speed

        # Move toward the player's vertical position (y-axis)
        if self.rect.y < player.rect.y:
            self.rect.y += self.speed
        elif self.rect.y > player.rect.y:
            self.rect.y -= self.speed

    def is_defeated(self):
        return self.health <= 0

    def draw_health_bar(self, screen):
        """Draw a health bar for the enemy."""
        max_health = 200 if self.is_boss else 50
        bar_length = 50
        bar_height = 5
        fill = (self.health / max_health) * bar_length
        border_rect = pygame.Rect(self.rect.x, self.rect.y - 10, bar_length, bar_height)
        fill_rect = pygame.Rect(self.rect.x, self.rect.y - 10, fill, bar_height)
        pygame.draw.rect(screen, (0, 255, 0), fill_rect)  # Green health bar
        pygame.draw.rect(screen, (255, 0, 0), border_rect, 2)  # Red border
