import pygame


class DebugOverlay:
    """
    A debug overlay that displays variables on the Pygame screen.

    :param screen: the Pygame screen to draw on
    :type screen: pygame.Surface
    """

    def __init__(self, screen):
        """
        Initializes the DebugOverlay with the given Pygame screen.

        :param screen: the Pygame screen to draw on
        :type screen: pygame.Surface
        """

        self.screen = screen
        self.font = pygame.font.SysFont('Courier New', 16, bold=True)
        self.variables = {}
        self.background_enabled = False
        self.overlay_surface = pygame.Surface(
            pygame.display.get_surface().get_size(),
            pygame.SRCALPHA
        )

    def add_variables(self, **kwargs):
        """
        Adds the given variables to the DebugOverlay.

        :param kwargs: the variables to add
        """

        for key, value in kwargs.items():
            self.variables[key] = value

    def remove_variables(self, *args):
        """
        Removes the specified variables from the DebugOverlay.

        :param args: the names of the variables to remove
        """

        for var_name in args:
            if var_name in self.variables:
                del self.variables[var_name]

    def set_font(self, name='Courier New', size=14, bold=False, italic=False):
        """
        Sets the font used by the DebugOverlay.

        :param name: the name of the font (default 'Courier New')
        :type name: str
        :param size: the size of the font (default 14)
        :type size: int
        :param bold: whether the font should be bold (default False)
        :type bold: bool
        :param italic: whether the font should be italic (default False)
        :type italic: bool
        :raises TypeError: if name is not a string or if size is not an integer
        """

        if not isinstance(name, str):
            raise TypeError("Font name must be a string")
        if not isinstance(size, int):
            raise TypeError("Font size must be an integer")
        self.font = pygame.font.SysFont(name, size, bold, italic)

    def enable_background(self):
        """
        Enables the background for the DebugOverlay.
        """

        self.background_enabled = True

    def disable_background(self):
        """
        Disables the background for the DebugOverlay.
        """

        self.background_enabled = False

    def draw(self):
        """
        Draws the DebugOverlay on the Pygame screen.
        """

        self.overlay_surface.fill((0, 0, 0, 0))

        y_offset = 0

        for var_name, value in self.variables.items():
            text = self.font.render(f"{var_name}: {value}", True, "white")
            if self.background_enabled:
                text_rect = text.get_rect()
                x, y = text_rect.left, text_rect.top + y_offset
                w, h = text_rect.width, text_rect.height
                pygame.draw.rect(self.overlay_surface, "black", (x, y, w, h))
            self.overlay_surface.blit(text, (0, y_offset))
            y_offset += self.font.get_linesize()

        self.screen.blit(self.overlay_surface, (0, 0))
