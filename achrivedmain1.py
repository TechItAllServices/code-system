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

    # ANSI escape code for resetting color
    RESET = "\033[0m"

    def display_alert(self, code, description, action):
        color = self.COLORS.get(code.upper(), "")
        reset_color = self.RESET

        # Formatting the alert message with colors
        formatted_alert = f"{color}Alert {code.upper()}: {description}\nAction: {action}{reset_color}"

        print(formatted_alert)

    def clear_alert(self):
        # Clearing the console screen
        print("\033[H\033[J")

# Creating an instance of the AlertSystem class
alert_system = AlertSystem()

# Reading actions from actions.txt file
def read_actions_file():
    try:
        with open("actions.txt", "r") as file:
            lines = file.readlines()
            if lines:
                return lines[0].strip()
    except FileNotFoundError:
        print("actions.txt file not found.")
    return ""

# Main function to process actions
def process_action(action):
    if action.startswith("-warn"):
        _, alert_type, reason = action.split(maxsplit=2)
        alert_system.display_alert(alert_type.upper(), "Alert", reason)
    elif action == "-clear":
        alert_system.clear_alert()
    else:
        print("Invalid command. Please use '-warn TYPE_HERE REASON_HERE' or '-clear'.")

if __name__ == "__main__":
    # Read actions from actions.txt and process
    action = read_actions_file()
    if action:
        process_action(action)
