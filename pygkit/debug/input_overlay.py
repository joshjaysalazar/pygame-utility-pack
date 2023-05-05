import pygame


class InputOverlay:
    def __init__(self, screen, expected_inputs=None):
        self.screen = screen
        self.expected_inputs = expected_inputs
        self.font = pygame.font.SysFont('Courier New', 16, bold=True)
        self.font_color = 'black'
        self.overlay_surface = pygame.Surface(
            self.screen.get_size(),
            pygame.SRCALPHA
        )
        self.current_inputs = set()

    def update_current_inputs(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.expected_inputs:
            keys_to_check = self.expected_inputs
        else:
            keys_to_check = range(len(pressed_keys))

        for key_code in keys_to_check:
            if pressed_keys[key_code]:
                self.current_inputs.add(key_code)
            else:
                self.current_inputs.discard(key_code)

    def draw(self, position):
        self.update_current_inputs()

        self.overlay_surface.fill((0, 0, 0, 0))

        if self.expected_inputs:
            inputs_to_draw = self.expected_inputs
        else:
            inputs_to_draw = list(self.current_inputs)

        text_surfaces = []
        for input_code in inputs_to_draw:
            input_name = pygame.key.name(input_code)
            input_detected = input_code in self.current_inputs
            input_color = self.font_color if input_detected else 'grey'
            text = self.font.render(input_name, True, input_color)
            text_surfaces.append(text)

        x_offset, y_offset = 0, 0
        space_between_keys = 5
        if position == 'topleft':
            x_offset = 0
            y_offset = 0
        elif position == 'topright':
            y_offset = 0
        elif position == 'bottomleft':
            x_offset = 0
            y_offset = self.screen.get_height() - self.font.get_linesize()
        elif position == 'bottomright':
            y_offset = self.screen.get_height() - self.font.get_linesize()

        for text in text_surfaces:
            if position == 'topright' or position == 'bottomright':
                x_offset = self.screen.get_width() - text.get_width() * len(text_surfaces) - space_between_keys * (len(text_surfaces) - 1)

            self.overlay_surface.blit(text, (x_offset, y_offset))
            x_offset += text.get_width() + space_between_keys

        self.screen.blit(self.overlay_surface, (0, 0))
