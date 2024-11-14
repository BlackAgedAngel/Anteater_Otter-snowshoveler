import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions (for pixel-perfect rendering)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the display with a specific resolution
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Your Game Title")

class SnowFlake:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(-50, -10)  # Start snowflakes above the screen
        self.size = random.randint(2, 7)
        self.speed = random.uniform(0.1, 0.3)  # Random speed between 0.3 and 1.0

    def update(self):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.reset()
    
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.x), int(self.y)), self.size)
    
    def reset(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(-50, -10)

# Load background image from assets folder and scale it to fit the screen
background_image = pygame.image.load('assets/background_image.jpg').convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Function to run the loading screen for 10 seconds
def show_loading_screen():
    running = True
    start_time = pygame.time.get_ticks()
    
    snowflakes = [SnowFlake() for _ in range(200)]  # Create a lot of snowflakes
    
    while running:
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        
        if elapsed_time >= 10:  # Transition to main game loop after 10 seconds
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.fill((0, 0, 0))  # Clear the screen with black color
        # Draw the background image scaled to fit the screen
        screen.blit(background_image, (0, 0))
        
        # Update and draw each snowflake
        for snowflake in snowflakes:
            snowflake.update()
            snowflake.draw(screen)

        # Update display
        pygame.display.flip()

    return True

# Main game loop function (placeholder for now)
def main_game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()

# Run the loading screen and then the main game loop
if __name__ == "__main__":
    show_loading_screen()
    main_game_loop()