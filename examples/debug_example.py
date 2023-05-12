import pygame
import sys
from pygkit.debug import DebugOverlay, InputOverlay, RectOverlay

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60


class Game:
    """A simple game that demonstrates the DebugOverlay class."""

    def __init__(self):
        """Initializes the game.
        
        Returns:
            None
        """

        # Initialize Pygame
        pygame.init()

        # Create the screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Debug Overlay Example")

        # Clock for controlling framerate
        self.clock = pygame.time.Clock()

        # Create 3 Circle instances of different sizes and colors
        self.circle1 = Circle(100, 100, 5, 5, 50, 50, "mediumpurple4")
        self.circle2 = Circle(200, 200, -4, -4, 100, 100, "darkorange")
        self.circle3 = Circle(300, 300, 3, -3, 150, 150, "darkgreen")

        # Create a sprite group and add the circles to it
        self.boxes = pygame.sprite.Group([self.circle1, self.circle2, self.circle3])

        # Initialize overlays
        self.debug_overlay = DebugOverlay()
        self.input_overlay = InputOverlay(
            expected_keys=[
                pygame.K_UP,
                pygame.K_DOWN,
                pygame.K_LEFT,
                pygame.K_RIGHT
            ],
            expected_mouse_buttons=[0, 2],
            show_mouse_position=True,
            expected_joystick_buttons=[
                [0, 0],
                [0, 1]
            ],
            expected_joystick_axes=[
                [0, 0]
            ]
        )
        self.rect_overlay = RectOverlay([self.boxes])

        # Set overlay fonts (debug_overlay uses default font)
        self.input_overlay.set_font(
                name="Arial",
                size=16,
                bold=True,
                italic=False,
                color="navy"
            )

    def run(self):
        """Runs the game. The 1 key toggles the debug overlay, the 2 key toggles
        the input overlay, the 3 key toggles the rect overlay
        
        Returns:
            None
        """

        # Main loop
        while True:
            # Event loop
            for event in pygame.event.get():
                # Check for quit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Check for 1 key press, toggle debug visibility if pressed
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    self.debug_overlay.visible = not self.debug_overlay.visible
                
                # Check for 2 key press, toggle input visibility if pressed
                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    self.input_overlay.visible = not self.input_overlay.visible

            # Draw background
            self.screen.fill("papayawhip")

            # Update and draw sprites
            self.boxes.update()
            self.boxes.draw(self.screen)

            # Draw the debug overlay in the top-left corner
            self.debug_overlay.draw(
                position="topleft",
                background_enabled=True,
                test_message="This is a test message.",
                fps=round(self.clock.get_fps(), 2),
                small_circle_x=self.circle1.rect.x,
                small_circle_y=self.circle1.rect.y,
                small_circle_vel=self.circle1.velocity
            )

            # Draw the input overlay in the bottom-left corner
            self.input_overlay.draw(
                position="bottomleft",
                background_enabled=False
                )
            
            # Draw the rect overlay
            self.rect_overlay.draw(
                collision_color="maroon",
                normal_color="blue",
                rect_width=2
            )

            # Update the display and limit the framerate
            pygame.display.flip()
            self.clock.tick(FPS)


class Circle(pygame.sprite.Sprite):
    """
    A simple sprite that moves around the screen.

    Args:
        x (int): The x-coordinate of the sprite's center.
        y (int): The y-coordinate of the sprite's center.
        x_vel (int): The sprite's velocity in the x-direction.
        y_vel (int): The sprite's velocity in the y-direction.
        width (int): The width of the sprite.
        height (int): The height of the sprite.
        color (tuple or str): The color of the sprite.
    
    Returns:
        None
    """

    def __init__(self, x, y, x_vel, y_vel, width, height, color):
        """Initializes the sprite.
        
        Returns:
            None
        """

        super().__init__()

        # Create the sprite's image and rect
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (width // 2, height // 2), width // 2)
        self.rect = self.image.get_rect(center=(x, y))

        # Set the sprite's velocity using a Vector2
        self.velocity = pygame.math.Vector2(x_vel, y_vel)

    def update(self):
        """Updates the sprite's position.
        
        Returns:
            None
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
if __name__ == "__main__":
    game = Game()
    game.run()
