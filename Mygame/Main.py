import pygame
import random
import time 

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
    background_image = pygame.image.load('assets/background_image.jpg').convert()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    

# Create a list to hold the snowflakes
snowflakes = [SnowFlake() for _ in range(500)]  # You can change the number of snowflakes here

def show_loading_screen():
    import pygame

    # Load font and create text surface with transparency
    font = pygame.font.SysFont("Arial", 60)
    text_surface = font.render("Loading Snow Journey :3", True, (0, 0, 0))
    

    # Load background image from assets folder and scale it to fit the screen
    background_image = pygame.image.load('Assets/background_image.jpg').convert()
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


def start_game():#test gameplay need to change a lot but we can keep movement
    screen_width = 640
    screen_height = 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    box_x = 100
    box_y = 100
    box_width = 50
    box_height = 50
    box_color = (255, 0, 0)  # red

    while True:
        # Handle events (e.g., keyboard, mouse)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Move the box (update its position)
        if pygame.key.get_pressed()[pygame.K_w]:
            box_y -= 5
        if pygame.key.get_pressed()[pygame.K_s]:
            box_y += 5
        if pygame.key.get_pressed()[pygame.K_a]:
            box_x -= 5
        if pygame.key.get_pressed()[pygame.K_d]:
            box_x += 5

        # Draw the box on the screen
        screen.fill((0, 0, 0))  # clear screen
        pygame.draw.rect(screen, box_color, (box_x, box_y, box_width, box_height))

        # Update the screen
        pygame.display.flip()
        pygame.time.Clock().tick(60)  # limit to 60 FPS


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

# Run the loading screen, then the message sequence, and then the main game loop
if __name__ == "__main__":
    show_loading_screen()
    time.sleep(1)
    main_game_loop()

