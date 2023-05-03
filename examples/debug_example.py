import pygame
import sys
from pygkit.debug import DebugOverlay

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

        # Create a Box instance
        self.sprite = Box(100, 100, 5, 5, 50, 50, "mediumpurple4")

    def run(self):
        """
        Runs the game. The V key toggles the debug overlay.

        :returns: None
        """

        # Main loop
        while True:
            # Event loop
            for event in pygame.event.get():
                # Check for quit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # Check for V key press, toggle debug visibility if pressed
                if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
                    # Toggle the debug overlay
                    self.debug.visible = not self.debug.visible

            # Draw background
            self.screen.fill("papayawhip")

            # Update and draw sprite
            self.sprite.update()
            self.screen.blit(self.sprite.image, self.sprite.rect)

            # Draw the top-left debug overlay
            self.debug.set_font(
                name="Courier New",
                size=16,
                bold=True,
                italic=False,
                color="white"
            )
            self.debug.draw(
                box_img=self.sprite.image,
                box_x=self.sprite.rect.x,
                box_y=self.sprite.rect.y,
                box_vel=self.sprite.velocity
            )

            # Draw the bottom-right debug overlay
            self.debug.set_font(
                name="Arial",
                size=20,
                bold=False,
                italic=True,
                color="navy"
            )
            self.debug.draw(
                position="bottomright",
                background_enabled=False,
                fps=round(self.clock.get_fps(), 2),
                test_message="This is a test message."
            )

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
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.velocity.x = -self.velocity.x
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity.y = -self.velocity.y
        elif self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity.y = -self.velocity.y


# Create the game object and run it
if __name__ == '__main__':
    game = Game()
    game.run()
