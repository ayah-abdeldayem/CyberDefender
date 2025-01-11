import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from PyQt5.QtCore import Qt


# Define scenarios
scenarios = [
    {
        "description": "Suspicious login detected from a foreign IP address.",
        "options": {
            "Block the user's account": "Correct! Blocking prevents unauthorized access.",
            "Ignore and monitor the situation": "Incorrect. Monitoring allows the attacker more time.",
            "Notify the user to verify the login": "Partially correct. Verifying adds a layer of security, but blocking is safer."
        },
        "correct": "Block the user's account"
    },
    {
        "description": "Malware detected on an employee's computer.",
        "options": {
            "Disconnect the computer from the network": "Correct! This prevents further spread.",
            "Run a full antivirus scan": "Incorrect. Scanning delays immediate containment.",
            "Notify all employees to check their devices": "Partially correct. It's useful, but immediate isolation is better."
        },
        "correct": "Disconnect the computer from the network"
    },
    {
        "description": "Unusual traffic spike detected from a server.",
        "options": {
            "Analyze the traffic and block suspicious IPs": "Correct! Blocking malicious IPs reduces risk.",
            "Reboot the server": "Incorrect. Rebooting doesn't address the root cause.",
            "Ignore and monitor the traffic": "Incorrect. Monitoring delays containment."
        },
        "correct": "Analyze the traffic and block suspicious IPs"
    },
    {
        "description": "Employee reported a phishing email.",
        "options": {
            "Warn all employees about the phishing attempt": "Correct! Awareness prevents further clicks.",
            "Delete the email and move on": "Incorrect. This doesn't inform others.",
            "Report the phishing email to authorities": "Partially correct. Reporting is good but not immediate."
        },
        "correct": "Warn all employees about the phishing attempt"
    }
]


class CyberDefenderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CyberDefender")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #1E1E2F; color: #00FF00; font-family: Courier New;")

        # Layout
        self.layout = QVBoxLayout()

        # Scenario label
        self.scenario_label = QLabel("Loading Scenario...", self)
        self.scenario_label.setAlignment(Qt.AlignCenter)
        self.scenario_label.setStyleSheet("font-size: 16px; color: #00FF00;")
        self.layout.addWidget(self.scenario_label)

        # Buttons for options
        self.buttons = []
        for i in range(3):  # 3 options per scenario
            btn = QPushButton("", self)
            btn.setStyleSheet("background-color: #333366; color: #00FF00; font-size: 14px;")
            btn.clicked.connect(lambda checked, b=i: self.check_response(b))
            self.layout.addWidget(btn)
            self.buttons.append(btn)

        # Next incident button
        self.next_button = QPushButton("Next Incident", self)
        self.next_button.setStyleSheet("background-color: #007ACC; color: #FFFFFF; font-size: 14px;")
        self.next_button.setEnabled(False)
        self.next_button.clicked.connect(self.next_scenario)
        self.layout.addWidget(self.next_button)

        self.setLayout(self.layout)

        # Initialize the first scenario
        self.current_scenario = 0
        self.load_scenario()

    def load_scenario(self):
        scenario = scenarios[self.current_scenario]
        
        # Update the scenario label
        self.scenario_label.setText(scenario["description"])

        # Update buttons with options
        for idx, (option, feedback) in enumerate(scenario["options"].items()):
            self.buttons[idx].setText(option)
            self.buttons[idx].setEnabled(True)

        # Disable the "Next Incident" button until a response is selected
        self.next_button.setEnabled(False)

    def check_response(self, selected_option_index):
        scenario = scenarios[self.current_scenario]
        selected_option = self.buttons[selected_option_index].text()
        feedback = scenario["options"][selected_option]

        # Show feedback in messagebox with cyber color theme
        if selected_option == scenario["correct"]:
            self.show_feedback("Correct!", feedback)
        else:
            self.show_feedback("Incorrect", feedback)

        # Disable buttons after a response
        for btn in self.buttons:
            btn.setEnabled(False)

        # Enable the "Next Incident" button after selecting an option
        self.next_button.setEnabled(True)

    def show_feedback(self, title, message):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information if title == "Correct!" else QMessageBox.Warning)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()

    def next_scenario(self):
        self.current_scenario += 1
        if self.current_scenario < len(scenarios):
            self.load_scenario()
        else:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Game Over")
            msg.setText("You have completed all incidents!")
            msg.exec_()
            self.close()


# Run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CyberDefenderApp()
    window.show()
    sys.exit(app.exec_())
