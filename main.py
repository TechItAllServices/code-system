import os
import subprocess
import time
from playsound import playsound

class AlertSystem:
    # ANSI color codes for different alerts
    COLORS = {
        "BLUE": "\033[94m",
        "GREEN": "\033[92m",
        "YELLOW": "\033[93m",
        "ORANGE": "\033[91m",
        "RED": "\033[31m",
        "BLACK": "\033[30;47m"
    }

    # Sound files for different alerts
    SOUNDS = {
        "BLUE": r"C:\Users\blues\Desktop\VSCode\serversclasses\Code_Blue.wav",
        "GREEN": r"C:\Users\blues\Desktop\VSCode\serversclasses\Code_Green.wav",
        "YELLOW": r"C:\Users\blues\Desktop\VSCode\serversclasses\Code_Yellow.mp3",
        "ORANGE": r"C:\Users\blues\Desktop\VSCode\serversclasses\Code_Orange.wav",
        "RED": r"C:\Users\blues\Desktop\VSCode\serversclasses\Code_Red.mp3",
        "BLACK": r"C:\Users\blues\Desktop\VSCode\serversclasses\Code_Black.mp3"
    }

    # ANSI escape code for resetting color
    RESET = "\033[0m"

    def display_alert(self, code, description, action):
        color = self.COLORS.get(code.upper(), "")
        reset_color = self.RESET

        # Formatting the alert message with colors
        formatted_alert = f"{color}Alert {code.upper()}: {description}\nAction: {action}{reset_color}"

        print(formatted_alert)

        # Play sound for the alert type
        sound_file = self.SOUNDS.get(code.upper(), "")
        if sound_file:
            playsound(sound_file)

    def clear_alert(self):
        # Clearing the console screen
        os_name = os.name
        if os_name == "nt":  # For Windows
            os.system("cls")
        else:  # For Linux, macOS, etc.
            os.system("clear")

# Creating an instance of the AlertSystem class
alert_system = AlertSystem()

# Function to continuously process actions
def process_actions():
    while True:
        try:
            with open("actions.txt", "r+") as file:
                lines = file.readlines()
                if lines:
                    action = lines[0].strip()
                    if action.startswith("-warn"):
                        _, alert_type, reason = action.split(maxsplit=2)
                        alert_system.display_alert(alert_type.upper(), "Alert", reason)
                    elif action == "-clear":
                        alert_system.clear_alert()
                    else:
                        print("Invalid command:", action)
                    # Clear the file after processing
                    file.seek(0)
                    file.truncate()
        except FileNotFoundError:
            print("actions.txt file not found.")
        except Exception as e:
            print("Error:", e)
        
        # Wait for one second before scanning again
        time.sleep(1)

if __name__ == "__main__":
    # Attempt to run the script with elevated permissions (if needed)
    try:
        command = f"runas /user:Administrator python {__file__}"
        subprocess.run(command, shell=True)
    except Exception as e:
        print("Error running with elevated permissions:", e)

    # Process actions continuously
    process_actions()
