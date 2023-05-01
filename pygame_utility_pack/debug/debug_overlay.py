import pygame

class DebugOverlay:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Courier New', 14)
        self.variables = []
        self.background_enabled = False
        self.overlay_surface = pygame.Surface(pygame.display.get_surface().get_size(), pygame.SRCALPHA)

    def add_variables(self, *args):
        for var in args:
            if var not in self.variables:
                self.variables.append(var)

    def remove_variables(self, *args):
        for var in args:
            if var in self.variables:
                self.variables.remove(var)

    def set_font(self, font_name='Courier New', font_size=14):
        if not isinstance(font_name, str) or not isinstance(font_size, int):
            raise ValueError("Font name must be a string and font size must be an integer")
        self.font = pygame.font.SysFont(font_name, font_size)

    def enable_background(self):
        self.background_enabled = True

    def disable_background(self):
        self.background_enabled = False

    def draw(self):
        self.overlay_surface.fill((0, 0, 0, 0))

        y_offset = 0

        fps_text = f"FPS: {pygame.time.Clock().get_fps():.1f}"
        fps_surface = self.font.render(fps_text, True, (255, 255, 255))
        if self.background_enabled:
            fps_rect = fps_surface.get_rect()
            pygame.draw.rect(fps_surface, (0, 0, 0), fps_rect, 0, 5)
        self.overlay_surface.blit(fps_surface, (0, y_offset))
        y_offset += self.font.get_linesize()

        for var in self.variables:
            text = self.font.render(f"{var=}".replace('=', ': '), True, (255, 255, 255))
            if self.background_enabled:
                text_rect = text.get_rect()
                pygame.draw.rect(text, (0, 0, 0), text_rect, 0, 5)
            self.overlay_surface.blit(text, (0, y_offset))
            y_offset += self.font.get_linesize()

        self.screen.blit(self.overlay_surface, (0, 0))
