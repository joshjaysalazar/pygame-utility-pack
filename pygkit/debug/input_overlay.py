import pygame
from pygkit.debug import DebugOverlay


class InputOverlay(DebugOverlay):
    def __init__(
            self,
            screen,
            expected_keys=None,
            expected_mouse_buttons=None,
            show_mouse_position=False,
            expected_joystick_buttons=None
        ):
        super().__init__(screen)

        # Member variables
        self.screen = screen
        self.expected_keys = expected_keys
        self.expected_mouse_buttons = expected_mouse_buttons
        self.show_mouse_position = show_mouse_position
        self.expected_joystick_buttons = expected_joystick_buttons

        # Set of currently active inputs
        self.current_keys = set()
        self.current_mouse_buttons = set()
        self.current_joystick_buttons = set()

        # Setup keyboard keys to check
        if self.expected_keys:
            self.keys_to_check = self.expected_keys
        else:
            self.keys_to_check = []
            for key in dir(pygame):
                if key.startswith("K_"):
                    self.keys_to_check.append(getattr(pygame, key))

        # Setup joystick buttons to check
        pygame.joystick.init()
        self.joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())] 

    def update_current_inputs(self):
        # Update keyboard inputs
        pressed_keys = pygame.key.get_pressed()
        for key_code in self.keys_to_check:
            if pressed_keys[key_code]:
                self.current_keys.add(key_code)
            else:
                self.current_keys.discard(key_code)
        
        # Update mouse inputs
        pressed_mouse_buttons = pygame.mouse.get_pressed(num_buttons=5)
        for button_code in range(len(pressed_mouse_buttons)):
            if pressed_mouse_buttons[button_code]:
                self.current_mouse_buttons.add(button_code)
            else:
                self.current_mouse_buttons.discard(button_code)

        # Update joystick inputs
        for i, joystick in enumerate(self.joysticks):
            for button_code in range(joystick.get_numbuttons()):
                id = (i, button_code)
                if joystick.get_button(button_code):
                    self.current_joystick_buttons.add(id)
                else:
                    self.current_joystick_buttons.discard(id)

    def get_text_surfaces(self):
        # Update current inputs
        self.update_current_inputs()

        # Set the keyboard inputs to draw
        if self.expected_keys:
            inputs_to_draw = self.expected_keys
        else:
            inputs_to_draw = list(self.current_keys)

        # Create text surfaces
        text_surfaces = []

        # Create surfaces for keyboard inputs
        for input_code in inputs_to_draw:
            input_name = pygame.key.name(input_code)
            if input_code in self.current_keys:
                input_color = self.font_color
            else:
                input_color = "grey"
            text = self.font.render(input_name.title(), True, input_color)
            text_surfaces.append(text)

        # Create surfaces for mouse buttons
        if self.expected_mouse_buttons:
            buttons_to_draw = self.expected_mouse_buttons
        else:
            buttons_to_draw = list(self.current_mouse_buttons)
        for button_code in buttons_to_draw:
            button_name = f"Mouse Button {button_code}"
            if button_code in self.current_mouse_buttons:
                button_color = self.font_color
            else:
                button_color = "grey"
            text = self.font.render(button_name, True, button_color)
            text_surfaces.append(text)

        # If show_mouse_position is True, create a surf for the mouse position
        if self.show_mouse_position:
            mouse_pos = pygame.mouse.get_pos()
            mouse_pos_str = f"Mouse Position: ({mouse_pos[0]}, {mouse_pos[1]})"
            text = self.font.render(mouse_pos_str, True, self.font_color)
            text_surfaces.append(text)

        # Create surfaces for joystick buttons
        if self.expected_joystick_buttons:
            buttons_to_draw = self.expected_joystick_buttons
        else:
            buttons_to_draw = list(self.current_joystick_buttons)
        for button_code in buttons_to_draw:
            button_name = f"Joystick {button_code[0]} Button {button_code[1]}"
            if button_code in self.current_joystick_buttons:
                button_color = self.font_color
            else:
                button_color = "grey"
            text = self.font.render(button_name, True, button_color)
            text_surfaces.append(text)
        
        return text_surfaces
