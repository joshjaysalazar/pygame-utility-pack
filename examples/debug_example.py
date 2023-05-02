import pygame
import sys
from pygame_utility_pack.debug.debug_overlay import DebugOverlay

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60


class Game:
    """
    A simple game that demonstrates the DebugOverlay class.
    """

    def __init__(self):
        """
        Initializes the game.

        :returns: None
        """

        # Initialize Pygame
        pygame.init()

        # Create the screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Debug Overlay Example")

        # Clock for controlling framerate
        self.clock = pygame.time.Clock()

        # Initialize DebugOverlay
        self.debug = DebugOverlay(self.screen)

        # Set custom font and font size for debug text
        self.debug.set_font('Consolas', 16)

        # Enable background for debug text
        self.debug.enable_background()

        # Create a Box instance
        self.sprite = Box(100, 100, 5, 5, 50, 50, "mediumpurple4")

        # Add sprite's position and velocity to the debug overlay
        self.debug.add_variables(
            sprite_rect=self.sprite.rect,
            sprite_velocity=self.sprite.velocity,
            bounces=self.sprite.bounces
        )

    def run(self):
        """
        Runs the game.

        :returns: None
        """

        # Main loop
        while True:
            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Draw background
            self.screen.fill("papayawhip")

            # Update and draw sprite
            self.sprite.update()
            self.screen.blit(self.sprite.image, self.sprite.rect)

            # Draw debug overlay
            self.debug.draw()

            # Update the display and limit the framerate
            pygame.display.flip()
            self.clock.tick(FPS)


class Box(pygame.sprite.Sprite):
    """
    A simple sprite that moves around the screen.

    :param x: The x-coordinate of the sprite's center.
    :type x: int
    :param y: The y-coordinate of the sprite's center.
    :type y: int
    :param width: The width of the sprite.
    :type width: int
    :param height: The height of the sprite.
    :type height: int
    :param color: The color of the sprite.
    :type color: tuple or str
    """

    def __init__(self, x, y, x_vel, y_vel, width, height, color):
        """
        Initializes the sprite.

        :param x: The x-coordinate of the sprite's center.
        :type x: int
        :param y: The y-coordinate of the sprite's center.
        :type y: int
        :param x_vel: The sprite's velocity in the x-direction.
        :type x_vel: int
        :param y_vel: The sprite's velocity in the y-direction.
        :type y_vel: int
        :param width: The width of the sprite.
        :type width: int
        :param height: The height of the sprite.
        :type height: int
        :param color: The color of the sprite.
        :type color: tuple or str
        :returns: None
        """
        super().__init__()

        # Create the sprite's image and rect
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))

        # Set the sprite's velocity using a Vector2
        self.velocity = pygame.math.Vector2(x_vel, y_vel)

        # Variable to keep track of how many times the sprite has bounced
        self.bounces = 0

    def update(self):
        """
        Updates the sprite's position.

        :returns: None
        """
        # Move the sprite
        self.rect.move_ip(self.velocity)

        # Check for collisions with screen boundaries and reverse if needed
        if self.rect.left < 0:
            self.rect.left = 0
            self.velocity.x = -self.velocity.x
            self.bounces += 1
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.velocity.x = -self.velocity.x
            self.bounces += 1
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity.y = -self.velocity.y
            self.bounces += 1
        elif self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity.y = -self.velocity.y
            self.bounces += 1


# Create the game object and run it
if __name__ == '__main__':
    game = Game()
    game.run()
