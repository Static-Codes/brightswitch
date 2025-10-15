from os import environ, path, system

home_dir = environ["HOME"]

if home_dir is None:
    home_dir = input("Please enter the path to your home directory:\n")

system_config_path = f"{home_dir}/.config"
xrandrb = "brightshift"
xrandr_path = "/usr/bin/xrandr"
app_config_path = path.join(system_config_path, xrandrb)
app_data_path = path.join(app_config_path, "data")
monitor_output_path = path.join(app_data_path, "monitor_output.txt")


def create_missing_dir(dir: str) -> bool:
    if (path.exists(dir)):
        return True

    try:
        return system(f"mkdir -p {dir}") == 0
    
    except Exception as e:
        print(e)
        return False

def create_missing_file(file: str) -> bool:
    if (path.exists(file)):
        return True
    
    try:
        return system(f"touch {file}") == 0
    
    except Exception as e:
        print(e)
        return False

create_missing_dir(app_config_path)
create_missing_dir(app_data_path)