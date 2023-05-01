import pygame
from pygame_utility_pack.debug.debug_overlay import DebugOverlay


pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Debug Overlay Example")

# MovingSprite class definition
class MovingSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = pygame.math.Vector2(200, 150)

    def update(self, dt):
        self.rect.x += self.velocity.x * dt
        self.rect.y += self.velocity.y * dt

# Create a MovingSprite instance
sprite = MovingSprite(100, 100, 50, 50, (255, 0, 0))

# Clock for controlling framerate
clock = pygame.time.Clock()

# Initialize DebugOverlay
debug = DebugOverlay(screen)

# Add sprite's position and velocity to the debug overlay
debug.add_variables(sprite.rect, sprite.velocity)

# Set custom font and font size
debug.set_font('Consolas', 16)

# Enable background for debug text
debug.enable_background()

running = True
while running:
    dt = clock.tick(60) / 1000  # Amount of seconds between each loop
    screen.fill((0, 0, 0))  # Clear the screen

    # Update and draw sprite
    sprite.update(dt)
    screen.blit(sprite.image, sprite.rect)

    # Check for collisions with screen boundaries and reverse direction if needed
    if sprite.rect.left < 0 or sprite.rect.right > screen_width:
        sprite.velocity.x = -sprite.velocity.x
    if sprite.rect.top < 0 or sprite.rect.bottom > screen_height:
        sprite.velocity.y = -sprite.velocity.y

    # Draw debug overlay
    debug.draw()

    pygame.display.flip()  # Update the display

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
