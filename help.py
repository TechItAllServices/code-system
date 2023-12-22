import os
os.system("clear")
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

# Creating an instance of the AlertSystem class
alert_system = AlertSystem()

# Displaying alerts
alert_system.display_alert("BLUE", "Normal Operations", "Normal activities permitted")
alert_system.display_alert("GREEN", "Scanning Protocol", "Individuals to be stopped and questioned if behaving suspiciously")
alert_system.display_alert("YELLOW", "Unauthorized Access Attempt", "Server admins to actively intervene and prevent unauthorized entry")
alert_system.display_alert("ORANGE", "Impending Breach", "Admins to intensify efforts to prevent breach. Non-admins advised to move to the safety domain")
alert_system.display_alert("RED", "Intrusion Detected", "Admins to report to the domain under attack. All non-essential personnel to evacuate to the safety domain immediately")
alert_system.display_alert("BLACK", "Complete Takeover", "Immediate evacuation of all personnel from the affected domain. No individuals should remain within the domain. Full evacuation to safety zones is mandatory")
