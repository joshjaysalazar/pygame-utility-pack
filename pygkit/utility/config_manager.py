import pygame
import configparser


class ConfigManager(dict):
    def __init__(self, file):
        super().__init__()

        # Load the settings
        self.load_settings(file)

    def load_settings(self, file):
        """Loads the settings from a config file.

        Args:
            file (str): The path to the config file.

        Returns:
            None
        """

        # Read the file
        config = configparser.ConfigParser()
        config.read(file)
        print(config.sections())

        # Iterate through the file
        for section in config.sections():
            # Create the section keys
            self[section] = {}

            # If the section is for keyboard controls, convert to Pygame keys
            keyboard_sections = ["key", "keys", "keyboard"]
            if section in keyboard_sections:
                for key, value in config.items(section):
                    self[section][key] = self.convert_to_key(value)

            # Otherwise, check the value type & convert, then add to dict
            else:
                for key, value in config.items(section):
                    # Check if int
                    if value.isdigit():
                        self[section][key] = int(value)

                    # Check if float
                    elif "." in value and value.replace(".", "", 1).isdigit():
                        self[section][key] = float(value)

                    # Check if bool
                    elif value.lower() == "true":
                        self[section][key] = True
                    elif value.lower() == "false":
                        self[section][key] = False

                    # If not int, float, or bool, assume str
                    else:
                        self[section][key] = str(value)
    
    def convert_to_key(self, key):
        """Converts a string key to a Pygame key constant. If the key is not
        recognized, it will return None.

        Args:
            key (str): The key to convert

        Returns:
            pygame.key: The converted key
        """

        # Check if the key is a single character
        if len(key) == 1:
            return getattr(pygame, "K_" + key.lower())

        # Check if the key is a special key
        else:
            return getattr(pygame, "K_" + key.upper(), None)