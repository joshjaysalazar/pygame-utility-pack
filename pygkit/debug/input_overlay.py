import pygame
from pygkit.debug import DebugOverlay


class InputOverlay(DebugOverlay):
    def __init__(self, screen, expected_inputs=None):
        super().__init__(screen)

        # Member variables
        self.screen = screen
        self.expected_inputs = expected_inputs

        # Set of currently active inputs
        self.current_inputs = set()

        # Setup keyboard keys to check
        if self.expected_inputs:
            self.keys_to_check = self.expected_inputs
        else:
            self.keys_to_check = []
            for key in dir(pygame):
                if key.startswith("K_"):
                    self.keys_to_check.append(getattr(pygame, key))

    def update_current_inputs(self):
        pressed_keys = pygame.key.get_pressed()

        for key_code in self.keys_to_check:
            if pressed_keys[key_code]:
                self.current_inputs.add(key_code)
            else:
                self.current_inputs.discard(key_code)

    def draw(self, position="topleft", background_enabled=True):
        # Return if the overlay is not visible
        if not self.visible:
            return
        
        self.update_current_inputs()

        # Clear the overlay surface
        self.overlay_surface.fill((0, 0, 0, 0))

        # Set the inputs to draw
        if self.expected_inputs:
            inputs_to_draw = self.expected_inputs
        else:
            inputs_to_draw = list(self.current_inputs)

        # Create text surfaces for variables
        text_surfaces = []
        for input_code in inputs_to_draw:
            input_name = pygame.key.name(input_code)
            input_detected = input_code in self.current_inputs
            input_color = self.font_color if input_detected else "grey"
            text = self.font.render(input_name, True, input_color)
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
