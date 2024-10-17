import pygame
from player import Player
from enemy import Enemy
from collectible import Collectible
from level import Level

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Side Scrolling Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_BLUE = (135, 206, 235)

# Game Variables
clock = pygame.time.Clock()
FPS = 60
FONT = pygame.font.SysFont('Arial', 24)

# Function to display text on the screen
def draw_text(text, font, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, (x, y))

# Function to wait for a specific key before starting the game
def wait_for_key_press():
    waiting = True
    screen.fill(WHITE)
    draw_text("Press ENTER to Start", FONT, RED, WIDTH // 2 - 100, HEIGHT // 2 - -140)
    draw_text(f'Instructions: "Left and right arrow key" for movement', FONT, BLACK, 150, 140)
    draw_text(f'"Space key" to jump', FONT, BLACK, 260, 170)
    draw_text(f'"F key" to shoot', FONT, BLACK, 260, 200)
    pygame.display.update()
    
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Wait for the Enter key to start the game
                    waiting = False

# Draw health bar for player and enemies
def draw_health_bar(x, y, health, max_health):
    bar_length = 100
    bar_height = 10
    fill = (health / max_health) * bar_length
    border_rect = pygame.Rect(x, y, bar_length, bar_height)
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(screen, GREEN, fill_rect)
    pygame.draw.rect(screen, BLACK, border_rect, 2)

# Error handling for image loading
def load_image(filepath, fallback_color=(255, 0, 0)):
    try:
        image = pygame.image.load(filepath)
        return image
    except pygame.error as e:
        print(f"Error loading image: {filepath}. Error: {e}")
        fallback_surface = pygame.Surface((50, 50))
        fallback_surface.fill(fallback_color)  # Fallback to a colored block if the image fails
        return fallback_surface

# Game over screen with restart option
def game_over_screen():
    screen.fill(WHITE)
    draw_text("Game Over!", FONT, RED, WIDTH // 2 - 65, HEIGHT // 2 - 50)
    draw_text("Press 'R' to Restart or 'Q' to Quit", FONT, BLACK, WIDTH // 2 - 150, HEIGHT // 2)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # Restart the game
                if event.key == pygame.K_q:
                    return False  # Quit the game

# Game Loop with Level Timer
def game_loop():
    try:
        player_img = load_image('assets/human.png')
        enemy_img = load_image('assets/enemy.png')
        boss_img = load_image('assets/boss.png')
        coin_img = load_image('assets/coins.png')
    except Exception as e:
        print(f"Error loading assets: {e}")
        return  # Exit if assets are missing or error occurs
    
    run = True
    player = Player(100, HEIGHT - 100, player_img)
    level_number = 1
    max_levels = 3
    score = 0

    # Timer for each level (in seconds)
    level_time_limit = {1: 10, 2: 10, 3: 10}  # Each level lasts 10 seconds
    level_start_time = pygame.time.get_ticks()  # Get the current time when the level starts

    # Start the first level
    level = Level(level_number)

    while run:
        clock.tick(FPS)
        screen.fill(LIGHT_BLUE)

        # Calculate the time left for the current level
        current_time = pygame.time.get_ticks()
        time_left = level_time_limit[level_number] - (current_time - level_start_time) // 1000

        # Display Score, Level, and Time Left
        draw_text(f'Score: {score}', FONT, BLACK, 10, 10)
        draw_text(f'Level: {level_number}', FONT, BLACK, 10, 40)
        draw_text(f'Time Left: {time_left} seconds', FONT, BLACK, 10, 70)
        draw_text(f'Health Bar:', FONT, BLACK, 10, 100)

        # Update player
        try:
            player.update(screen)
        except Exception as e:
            print(f"Error updating player: {e}")

        # Update level and enemies
        try:
            score += level.update(screen, player)

            # Check for collisions between projectiles and enemies
            for projectile in player.projectiles[:]:
                for enemy in level.enemies[:]:
                    if projectile.check_collision(enemy):
                        player.projectiles.remove(projectile)  # Remove projectile if it hits an enemy
                        if enemy.is_defeated():
                            level.enemies.remove(enemy)  # Remove enemy if defeated
                            score += 10  # Increase score for defeating an enemy
        except Exception as e:
            print(f"Error updating level: {e}")

        # Draw player's health bar
        draw_health_bar(115, 110, player.health, 100)

        # Check if the player runs out of health
        if player.health <= 0:
            if game_over_screen():
                wait_for_key_press()  # Return to the waiting screen after game over
                game_loop()  # Restart the game loop
                return  # Exit the current loop to avoid nested loops
            else:
                run = False

        # Check if the level is complete either by time running out or defeating all enemies
        elif level.level_complete() or time_left <= 0:
            level_number += 1
            if level_number > max_levels:
                draw_text('YOU WIN!', FONT, WHITE, WIDTH // 2 - 50, HEIGHT // 2)
                pygame.display.update()
                pygame.time.wait(3000)
                run = False
            else:
                level = Level(level_number)
                level_start_time = pygame.time.get_ticks()  # Reset the timer for the next level

        # Handle events
        for event in pygame.event.get():
            try:
                if event.type == pygame.QUIT:
                    run = False
            except Exception as e:
                print(f"Error handling event: {e}")

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    try:
        wait_for_key_press()  # Wait for the key press before starting the game loop
        game_loop()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        pygame.quit()
