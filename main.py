#!/usr/bin/env python3

from display import Display, DisplayManager, List
from sys import argv

help_message = """
x = Monitor Name (See brightswitch --help) 
y = Brightness (A float representing the desired brightness)

Supported Commands
    - brightswitch --monitor==(x) --brightness==(y)
        - Change the specified monitor to the specified brightness | 0 < y <= 1

    - brightswitch --all --brightness==(y)
        - Change ALL monitors to the specified brightness | 0 < y <= 1

    - brightswitch --list
        - Lists the port identifiers associated with each monitor (Recommended to get these directly from your distro's display manager)
"""

displaym = DisplayManager()
displaym.set_displays()

def main():
    if (2 > len(argv) < 4):
        print("Invalid command, for more information, please type:\nbrightswitch --help")
        exit(1)
    
    handle_commands(argv)

def handle_commands(args: List[str]):
    if len(args) == 2 and args[1] == "--help":
        print(help_message)
        exit(0)
    
    elif len(args) == 2 and args[1] == "--list" and len(displaym._displays) == 0:
        print("Unable to query active displays. ")
        exit(1)

    elif len(args) == 2 and args[1] == "--list" and len(displaym._displays) > 0:
        for display in displaym._displays:
            print(f"{display}\n")
        exit(0)
    
    elif len(args) == 3 and args[1].startswith("--monitor==") and args[2].startswith("--brightness=="):
        monitor_id = args[1].replace("--monitor==", "")
        new_bright_raw = args[2].replace("--brightness==", "")
        
        try:
            if monitor_id not in displaym._displays.__repr__():
                print(
                    f"Invalid monitor identifier, '{monitor_id}', expected one of the following:",
                    "{", ".join([display._name for display in displaym._displays])}"
                )
                exit()

            new_brightness = float(new_bright_raw)
            requested_display = displaym.get_display_by_name(monitor_id)
            
            if requested_display is None:
                print("Unable to access the requested display.")
            requested_display.update_brightness(new_brightness)
            exit(0)
                
        except Exception as e:
            print(e)
            print("Invalid brightness value provided, must be a number greater than 0.0 and less than or equal to 100.0")
            exit()

    elif len(args) == 3 and args[1].startswith("--all") and args[2].startswith("--brightness=="):
        new_value_raw = args[2].replace("--brightness==", "")
        
        try:
            new_value = float(new_value_raw)
            for i in range(0, len(displaym._displays)):
                displaym._displays[i].update_brightness(new_value)
            exit()
                
        except Exception as e:
            print(e)
            print("Invalid brightness value provided, must be a number greater than 0.0 and less than or equal to 100.0")
            exit()
        


        

if __name__ == "__main__":
    main()
    # displays = DisplayManager().get_displays()
    # print(displays)
