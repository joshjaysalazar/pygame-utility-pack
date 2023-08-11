import configparser
import sys


class ConfigurationManager(dict):
    def __init__(self, file):
        super().__init__()

        # Load the settings
        self.load_settings(file)

    def load_settings(self, file):
        # Read the file
        config = configparser.ConfigParser()
        config.read(file)

        # Iterate through the file
        for section in config.sections():
            # Create the section keys
            self[section] = {}

            # Check the value type & convert accordingly, then add to dict
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

# test = ConfigurationManager("test.ini")