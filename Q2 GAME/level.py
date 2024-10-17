import pygame
from enemy import Enemy
from collectible import Collectible
import random

class Level:
    def __init__(self, level_number=1):
        self.level_number = level_number
        if level_number < 3:
            # Normal enemies for levels 1 and 2
            self.enemies = [
                Enemy(400 + i * 200, 550, pygame.image.load('assets/enemy.png')) for i in range(level_number + 2)
            ]
        else:
            # Three boss enemies in Level 3, which follow the player
            self.enemies = [Enemy(random.randint(100, 700), random.randint(100, 500), pygame.image.load('assets/boss.png'), is_boss=True) for i in range(3)]

        # Adding more collectibles based on the level number
        self.collectibles = [
            Collectible(300 + i * 150, 550, pygame.image.load('assets/coins.png')) for i in range(level_number + 3)
        ]

    def update(self, screen, player):
        score = 0
        for enemy in self.enemies:
            enemy.update(screen, player)  # Enemies follow the player's movement
            if player.rect.colliderect(enemy.rect):
                player.health -= 1  # Damage player on collision
            if enemy.is_defeated():
                score += 10  # Add points for defeated enemies
                self.enemies.remove(enemy)

        for collectible in self.collectibles:
            if not collectible.collected:
                collectible.update(screen, player)
                if collectible.collected:
                    score += 5  # Add points for collected items
                    player.health = min(100, player.health + 10)  # Restore health

        return score

    def level_complete(self):
        return all([enemy.is_defeated() for enemy in self.enemies]) and \
               all([collectible.collected for collectible in self.collectibles])
