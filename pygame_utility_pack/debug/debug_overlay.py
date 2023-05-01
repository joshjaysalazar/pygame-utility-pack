import pygame

class DebugOverlay:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Courier New', 16, bold=True)
        self.variables = {}
        self.background_enabled = False
        self.overlay_surface = pygame.Surface(pygame.display.get_surface().get_size(), pygame.SRCALPHA)

    def add_variables(self, **kwargs):
        for key, value in kwargs.items():
            self.variables[key] = value

    def remove_variables(self, *args):
        for var_name in args:
            if var_name in self.variables:
                del self.variables[var_name]

    def set_font(self, name='Courier New', size=14, bold=False, italic=False):
        if not isinstance(name, str) or not isinstance(size, int):
            raise ValueError("Font name must be a string and font size must be an integer")
        self.font = pygame.font.SysFont(name, size, bold, italic)

    def enable_background(self):
        self.background_enabled = True

    def disable_background(self):
        self.background_enabled = False

    def draw(self):
        self.overlay_surface.fill((0, 0, 0, 0))

        y_offset = 0

        for var_name, value in self.variables.items():
            text = self.font.render(f"{var_name}: {value}", True, (255, 255, 255))
            if self.background_enabled:
                text_rect = text.get_rect()
                pygame.draw.rect(self.overlay_surface, (0, 0, 0), (text_rect.left, text_rect.top + y_offset, text_rect.width, text_rect.height))
            self.overlay_surface.blit(text, (0, y_offset))
            y_offset += self.font.get_linesize()

        self.screen.blit(self.overlay_surface, (0, 0))
