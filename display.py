from collections.abc import MutableSequence
from directory_manager import (
    app_data_path, 
    create_missing_dir, 
    create_missing_file, 
    monitor_output_path, 
    path, 
    system, 
    xrandr_path
)

from re import compile, findall
from typing import List, Optional

import platform


class Display():
    def __init__(self, name: str):
        self._name: str = name
        self._brightness: float = 1.00

    def __repr__(self) -> str:
        return f"Connection Name: {self._name}\nBrightness: {self.convert_to_fraction()} ({self.convert_to_percent()})"
        
    
    def convert_to_percent(self) -> str:
        return f"{(self._brightness * 100.0):.2f}%"
    
    def convert_to_fraction(self) -> str:
        return f"{self._brightness:.2f}/1.00"

    def is_valid_brightness(self, new_value: float) -> bool:
        return 0 < new_value <= 1

    def update_brightness(self, new_value: float):
        if (self.is_valid_brightness(new_value)):
            self._brightness = new_value
            change_brightness_cmd = f"xrandr --output {self._name} --brightness {new_value}"
            
            if system(change_brightness_cmd) == 0:
                print(
                    f"Updated Monitor '{self._name}'",
                    f"using command:\n{change_brightness_cmd}\n\n"
                    f"New value:\n{self.convert_to_fraction()} ({self.convert_to_percent()})\n"
                )

            else:
                print(f"Unable to update Monitor {self._name} brightness using command:\n{change_brightness_cmd}")
                exit()
        else:
            print("Invalid brightness value provided, must be a number greater than 0 and less than or equal to 1.00\n")
            print("Common Values:")
            print("0.25 -> 25%")
            print("0.50 -> 50%")
            print("0.75 -> 75%")
            print("1 -> 100%")
    




class DisplayManager():
    active_display_cmd = f"xrandr --listactivemonitors > {monitor_output_path}"
    monitor_cmd_output = None

    def __init__(self):
        self._displays: MutableSequence[Display] = []

    def get_display_by_name(self, name) -> "Display":
        if len(self._displays) == 0:
            print("Unable to query active displays.")

        for display in self._displays:
            if display._name == name:
                return display

    def parse(self, output: List[str]):
        try:
            matches = findall("\\s{2}((?:eDP|DP|HDMI|VGA)-[0-9])", "\n".join(output))
            return matches

        except Exception as e:
            print(e)
            return []


    def set_displays(self):
        if (platform.system() != 'Linux'):
            raise Exception("Invalid OS, this project was designed for Modern Debian-Based Linux Distros.")
        
        elif (not path.exists(xrandr_path)):
            raise Exception("This project was designed for Modern Debian-Based Linux Distros.")

        try:
            system(self.active_display_cmd)
            if (not path.exists(monitor_output_path) and not create_missing_file(monitor_output_path)):
                raise Exception(f"Unable to determine active displays, using command:\n{self.active_display_cmd}")
            
            with open(monitor_output_path, "r") as file:
                monitor_cmd_output = file.readlines()

            if (monitor_cmd_output is None):
                raise Exception(f"Unable to determine active displays, using command:\n{self.active_display_cmd}\nNull output.")

            display_names = self.parse(monitor_cmd_output)
            self._displays = [Display(name) for name in display_names]

        except Exception as e:
            print(e)
            exit()
