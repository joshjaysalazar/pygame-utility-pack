import pygame


class DebugOverlay:
    """A debug overlay that displays variables on the Pygame screen.

    Args:
        screen (pygame.Surface): The Pygame screen to draw on.
    """

    def __init__(self, screen):
        """Initializes the DebugOverlay with the given Pygame screen.

        Args:
            screen (pygame.Surface): The Pygame screen to draw on.

        Returns:
            None
        """

        # Member variables
        self.screen = screen

        # Default font for the DebugOverlay
        self.font = pygame.font.SysFont("Courier New", 16, bold=True)

        # Variable to track font color
        self.font_color = "white"

        # Flag indicating whether the DebugOverlay is visible
        self.visible = True

        # Surface used to draw the DebugOverlay, set to the size of the screen
        self.overlay_surface = pygame.Surface(
            pygame.display.get_surface().get_size(),
            pygame.SRCALPHA
        )

    def set_font(self, **options):
        """Sets the font used by the DebugOverlay.

        Args:
            **options: The options for the font.

        Raises:
            ValueError: If an invalid option is provided.
            TypeError: If an option has an invalid type.

        Returns:
            None
        """

        default_options = {
            "name": "Courier New",
            "size": 14,
            "bold": False,
            "italic": False,
            "color": "white"
        }

        # Update the default options with the provided options
        for key, value in options.items():
            if key in default_options:
                default_options[key] = value
            else:
                raise ValueError(f"Invalid option \"{key}\"")

        # Check for invalid arguments
        if not isinstance(default_options["name"], str):
            raise TypeError("Font name must be a string")
        if not isinstance(default_options["size"], int):
            raise TypeError("Font size must be an integer")
        if not isinstance(default_options["bold"], bool):
            raise TypeError("Font bold flag must be a boolean")
        if not isinstance(default_options["italic"], bool):
            raise TypeError("Font italic flag must be a boolean")
        if not isinstance(default_options["color"], str):
            raise TypeError("Font color must be a string")

        # Set the font and color
        self.font = pygame.font.SysFont(
            default_options["name"],
            default_options["size"],
            default_options["bold"],
            default_options["italic"]
        )
        self.font_color = default_options["color"]

    def toggle_visible(self, enabled=None):
        """Toggles the visibility of the DebugOverlay.

        Args:
            enabled (bool, optional): Whether to enable the overlay 
                (default None).

        Returns:
            None
        """

        # Toggle the visibility if enabled is None, or set it to the given value
        if enabled is None:
            self.visible = not self.visible
        else:
            self.visible = enabled

    def draw(self, position="topleft", background_enabled=True, **variables):
        """Draws the DebugOverlay on the Pygame screen.

        Args:
            position (str, optional): The position of the debug text 
                (default "topleft").
            background_enabled (bool, optional): Whether to draw a background 
                behind the text (default True).
            **variables: The variables to display on the overlay.

        Raises:
            ValueError: If an invalid position is provided.

        Returns:
            None
        """

        # Return if the overlay is not visible
        if not self.visible:
            return

        # Clear the overlay surface
        self.overlay_surface.fill((0, 0, 0, 0))

        # Create text surfaces for variables
        text_surfaces = []
        for var_name, value in variables.items():
            text = self.font.render(
                f"{var_name}: {value}",
                True,
                self.font_color
            )
            text_surfaces.append(text)

        # Calculate the total height of the text surfaces
        total_height = len(text_surfaces) * self.font.get_linesize()

        # Determine the x and y offsets based on the position
        if position == "topleft":
            x_offset = 0
            y_offset = 0
        elif position == "topright":
            y_offset = 0
        elif position == "bottomleft":
            x_offset = 0
            y_offset = self.screen.get_height() - total_height
        elif position == "bottomright":
            y_offset = self.screen.get_height() - total_height
        else:
            raise ValueError(
                "Invalid position. Must be \"topleft\", \"topright\", " \
                "\"bottomleft\", or \"bottomright\"."
            )

        # Draw the text surfaces on the overlay surface
        for text in text_surfaces:
            if position == "topright" or position == "bottomright":
                x_offset = self.screen.get_width() - text.get_width()

            if background_enabled:
                text_rect = text.get_rect()
                x, y = x_offset + text_rect.left, y_offset + text_rect.top
                w, h = text_rect.width, text_rect.height
                pygame.draw.rect(self.overlay_surface, "black", (x, y, w, h))

            self.overlay_surface.blit(text, (x_offset, y_offset))
            y_offset += self.font.get_linesize()

        # Draw the overlay surface on the Pygame screen
        self.screen.blit(self.overlay_surface, (0, 0))
