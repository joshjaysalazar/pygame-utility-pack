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

    def get_text_surfaces(self):
        self.update_current_inputs()

        # Set the inputs to draw
        if self.expected_inputs:
            inputs_to_draw = self.expected_inputs
        else:
            inputs_to_draw = list(self.current_inputs)

        # Create text surfaces for variables
        text_surfaces = []
        for input_code in inputs_to_draw:
            input_name = pygame.key.name(input_code)
            if input_code in self.current_inputs:
                input_color = self.font_color
            else:
                input_color = "grey"
            text = self.font.render(input_name, True, input_color)
            text_surfaces.append(text)
        
        return text_surfaces
