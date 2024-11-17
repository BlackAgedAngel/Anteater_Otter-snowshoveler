import pygame
import random
import time 
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get script's directory

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
        self.y = random.randint(0, SCREEN_HEIGHT)  # Start snowflakes above the screen
        self.size = random.randint(2, 7)
        self.speed = random.uniform(0.1, 0.3)

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
    background_image = pygame.image.load(os.path.join(BASE_DIR, 'assets', 'background_image.jpg'))
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    

# Create a list to hold the snowflakes
snowflakes = [SnowFlake() for _ in range(500)]  # You can change the number of snowflakes here

def show_loading_screen():
    import pygame

    # Load font and create text surface with transparency
    font = pygame.font.SysFont("Arial", 60)
    text_surface = font.render("Loading Snow Journey :3", True, (0, 0, 0))
    

    # Load background image from assets folder and scale it to fit the screen
    background_image = pygame.image.load(os.path.join(BASE_DIR, 'assets', 'background_image.jpg'))
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Center the text on the screen
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150))

    running = True 

    while running:
        start_time = 0
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        
        if elapsed_time >= 1:  # Transition to main game loop after 5 seconds
            running = False

        screen.blit(background_image, (0, 0))  # Draw background image first
        screen.fill((0, 0, 0), special_flags=pygame.BLEND_RGBA_SUB)  # Clear the screen with a black color but maintain transparency
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        # Update and draw each snowflake
        for snowflake in snowflakes:
            snowflake.update()
            snowflake.draw(screen)
        screen.blit(text_surface, text_rect)  # Draw the loading text on top
        
        # Update display
        pygame.display.flip()


    return True

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class TextSequence():
 

    def __init__(self, messages):
        self.messages = messages  # List of messages to display
        self.current_message_index = 0  # Start with the first message
        self.font = pygame.font.SysFont("Arial", 30)
        

    def draw(self, surface):
        # Render the current message
        if self.current_message_index < len(self.messages):
            message = self.messages[self.current_message_index]
            text_surface = self.font.render(message, True, WHITE)
            text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            surface.blit(text_surface, text_rect)

    def next_message(self):
        # Move to the next message, if there is one
        if self.current_message_index < len(self.messages) - 1:
            self.current_message_index += 1

    def is_finished(self):
        # Check if we've shown all messages
        return self.current_message_index >= len(self.messages) - 1


# Sample messages for the sequence
intro_messages = [
    "You wake up on a fine winter's morn.",
    "Your stomach growls, it craves sustanance.",
    "But alas, one problem persists.",
    "You have no money.",
    "You're broke.",
    "And the world is not your oyster.",
    "You decide you must make some money.",
    "So time to shovel some snow.",
    "Each pile of snow shoveled will earn you $1.",
    "Get ready to start shoveling!"
]


def start_game():
    pygame.init()

    # Screen dimensions
    screen_width = 640
    screen_height = 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Winter Driveway Game")

    # Load the character sprite
    character_sprite = pygame.image.load(os.path.join(BASE_DIR, 'assets', 'Otter_Player.png')).convert_alpha()  # Ensure the sprite has transparency
    
    # Scale the sprite to fit better in the game window (resize to 50x50 as an example)
    sprite_width = 50
    sprite_height = 50
    character_sprite = pygame.transform.scale(character_sprite, (sprite_width, sprite_height))

    # Initial character position
    char_x = 100
    char_y = 100
    char_speed = 5  # Movement speed

    # Create snowflakes
    snowflakes = [Snowflake_2(screen_width, screen_height) for _ in range(100)]

    # Game loop
    while True:
        # Handle events (e.g., keyboard, mouse)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Move the character (update its position)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            char_y -= char_speed
        if keys[pygame.K_s]:
            char_y += char_speed
        if keys[pygame.K_a]:
            char_x -= char_speed
        if keys[pygame.K_d]:
            char_x += char_speed

        # Prevent the character from moving out of bounds
        char_x = max(0, min(char_x, screen_width - sprite_width))
        char_y = max(0, min(char_y, screen_height - sprite_height))

        # Draw the winter driveway as the background
        draw_winter_driveway(screen, screen_width, screen_height, snowflakes)

        # Draw the character sprite on top of the background
        screen.blit(character_sprite, (char_x, char_y))

        # Update the screen
        pygame.display.flip()
        pygame.time.Clock().tick(60)  # Limit to 60 FPS

        # Draw the winter driveway as the background
        draw_winter_driveway(screen, screen_width, screen_height, snowflakes)

        # Draw the character sprite on top of the background
        screen.blit(character_sprite, (char_x, char_y))

        # Update the screen
        pygame.display.flip()
        pygame.time.Clock().tick(60)  # Limit to 60 FPS



# Create an instance of TextSequence with the intro messages
text_sequence = TextSequence(intro_messages)

# Main game loop function
def main_game_loop():
    running = True
    while running:


        screen.fill(BLACK)  # Clear screen with black background
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if text_sequence.is_finished():
                    running = False  # End the sequence to start the game
                else:
                    text_sequence.next_message()

        # Draw the current message on the screen
        text_sequence.draw(screen)

        # Update display
        pygame.display.flip()

    # Transition to the main game (currently empty placeholder)
    start_game()


        
#def start_game():
    # Placeholder for the main game loop
    running = True
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.flip()

    pygame.quit()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Snowflake class for gameplay
class Snowflake_2:
    def __init__(self, width, height):
        self.x = random.randint(0, width)
        self.y = random.randint(-50, height)
        self.size = random.randint(2, 5)
        self.speed = random.uniform(1, 3)

    def fall(self, height):
        self.y += self.speed
        if self.y > height:
            self.y = random.randint(-50, -10)
            self.x = random.randint(0, SCREEN_WIDTH)

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (self.x, self.y), self.size)

# Driveway for scene 1
def draw_winter_driveway(surface, width, height, snowflakes):
    """
    Draws a winter driveway scene with a house, driveway, and snowflakes.

    Args:
        surface (pygame.Surface): The surface to draw on.
        width (int): The width of the scene.
        height (int): The height of the scene.
        snowflakes (list): A list of Snowflake objects for the scene.
    """
    # Fill the screen with white for the winter theme
    surface.fill(WHITE)
    
    # Draw the driveway (a large gray rectangle)
    pygame.draw.rect(surface, GRAY, (100, 200, width - 200, height - 200))
    
    # Draw borders on the driveway
    pygame.draw.line(surface, BLACK, (100, 200), (100, height), 5)  # Left border
    pygame.draw.line(surface, BLACK, (width - 100, 200), (width - 100, height), 5)  # Right border
    
    # Draw lane lines
    lane_width = (width - 200) // 3
    for i in range(1, 3):  # Two lane lines
        x_pos = 100 + lane_width * i
        pygame.draw.line(surface, WHITE, (x_pos, 200), (x_pos, height), 3)
    
    # House dimensions
    house_width = 300
    house_height = 150
    roof_height = 40
    house_x = (width - house_width) // 2  # Center the house horizontally
    house_y = 50  # Fixed height from the top
    
    # Draw the house
    pygame.draw.rect(surface, GRAY, (house_x, house_y, house_width, house_height))  # Main body
    pygame.draw.rect(surface, BLACK, (house_x, house_y, house_width, house_height), 3)  # Outline
    pygame.draw.polygon(surface, GRAY, [
        (house_x, house_y), 
        (house_x + house_width // 2, house_y - roof_height), 
        (house_x + house_width, house_y)
    ])  # Roof
    pygame.draw.polygon(surface, BLACK, [
        (house_x, house_y), 
        (house_x + house_width // 2, house_y - roof_height), 
        (house_x + house_width, house_y)
    ], 3)  # Roof outline
    pygame.draw.rect(surface, WHITE, (house_x + 50, house_y + 50, 50, 50))  # Left window
    pygame.draw.line(surface, BLACK, (house_x + 50, house_y + 75), (house_x + 100, house_y + 75), 2)  # Window detail
    pygame.draw.line(surface, BLACK, (house_x + 75, house_y + 50), (house_x + 75, house_y + 100), 2)
    pygame.draw.rect(surface, WHITE, (house_x + 200, house_y + 50, 50, 50))  # Right window
    pygame.draw.line(surface, BLACK, (house_x + 200, house_y + 75), (house_x + 250, house_y + 75), 2)
    pygame.draw.line(surface, BLACK, (house_x + 225, house_y + 50), (house_x + 225, house_y + 100), 2)
    pygame.draw.rect(surface, WHITE, (house_x + 125, house_y + 100, 50, 50))  # Door
    pygame.draw.rect(surface, BLACK, (house_x + 125, house_y + 100, 50, 50), 3)
    
    # Draw snowflakes
    for snowflake in snowflakes:
        snowflake.fall(height)
        snowflake.draw(surface)

# Run the loading screen, then the message sequence, and then the main game loop
if __name__ == "__main__":
    show_loading_screen()
    time.sleep(1)
    main_game_loop()
