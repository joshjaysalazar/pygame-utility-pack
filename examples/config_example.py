import pygame
import sys
from pygkit.utility import ConfigManager


class Game:
    """A simple game that demonstrates the debug overlay classes."""

    def __init__(self):
        """Initializes the game.
        
        Returns:
            None
        """

        # Initialize Pygame
        pygame.init()

        # Load the config file
        self.config = ConfigManager("settings.ini")
        print(self.config)

        # Create the screen
        self.screen = pygame.display.set_mode(
            (self.config["display"]["width"], self.config["display"]["height"])
        )
        pygame.display.set_caption("Configuration Manager Example")

        # Clock for controlling framerate
        self.clock = pygame.time.Clock()

        # Create 3 Circle instances of different sizes and colors
        self.player = Player(self.config)

    def run(self):
        """Runs the game.

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

            # Draw background
            self.screen.fill(self.config["display"]["background_color"])

            # Update and draw the player
            self.player.update()
            self.screen.blit(self.player.image, self.player.rect)

            # Update the display and limit the framerate
            pygame.display.flip()
            self.clock.tick(self.config["display"]["fps"])


class Player(pygame.sprite.Sprite):
    """A simple sprite that can be controlled with the keys in the config.
    
    Args:
        config (ConfigManager): The config manager instance.
    """

    def __init__(self, config):
        """Initializes the sprite.
        
        Returns:
            None
        """

        super().__init__()

        # Member variables
        self.config = config

        # Create the sprite's image and rect
        self.image = pygame.Surface(
            (self.config["player"]["width"], self.config["player"]["height"])
        )
        self.image.fill(self.config["player"]["color"])

        # Calculate the center of the screen and place the player there
        center = (
            self.config["display"]["width"] // 2,
            self.config["display"]["height"] // 2
        )
        self.rect = self.image.get_rect(center=center)

    def update(self):
        """Updates the sprite's position.
        
        Returns:
            None
        """

        # Move the sprite if the given keys in the config are pressed
        keys = pygame.key.get_pressed()
        if keys[self.config["keyboard"]["up"]]:
            self.rect.move_ip(0, -self.config["player"]["speed"])
        if keys[self.config["keyboard"]["down"]]:
            self.rect.move_ip(0, self.config["player"]["speed"])
        if keys[self.config["keyboard"]["left"]]:
            self.rect.move_ip(-self.config["player"]["speed"], 0)
        if keys[self.config["keyboard"]["right"]]:
            self.rect.move_ip(self.config["player"]["speed"], 0)

# Create the game object and run it
if __name__ == "__main__":
    game = Game()
    game.run()
