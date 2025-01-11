import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

# Define different technical scenarios
scenarios = [
    {
        "description": "Suspicious login detected from a foreign IP address.",
        "logs": [
            "2025-01-11 17:03:12.245 User 'admin' login attempt from IP 172.16.254.1.",
            "2025-01-11 17:04:23.789 Login failed. Invalid credentials.",
            "2025-01-11 17:05:45.346 Attempt detected from foreign IP: 190.56.78.120."
        ],
        "options": {
            "Block the user's account": "Correct! Blocking prevents unauthorized access immediately.",
            "Ignore and monitor the situation": "Incorrect. Ignoring allows the attacker more time to exploit vulnerabilities.",
            "Notify the user to verify the login": "Partially correct. Verifying the login adds an extra layer, but blocking is more secure."
        },
        "correct": "Block the user's account",
        "explanation": "Blocking immediately prevents the attacker from accessing the system."
    },
    {
        "description": "Malware detected on an employee's computer.",
        "logs": [
            "2025-01-11 17:06:00 Malware alert triggered on device 'employee01'.",
            "2025-01-06 17:06:30 Antivirus scan in progress...",
            "2025-01-11 17:07:00 High-risk malware detected. Action required."
        ],
        "options": {
            "Disconnect the computer from the network": "Correct! Isolating the device prevents further spread of malware.",
            "Run a full antivirus scan": "Incorrect. Scanning is important but takes time. Immediate isolation is more effective.",
            "Notify all employees to check their devices": "Partially correct. It's important, but isolating the infected device prevents further damage."
        },
        "correct": "Disconnect the computer from the network",
        "explanation": "Disconnecting prevents the malware from communicating with external servers and spreading to other devices."
    },
    {
        "description": "Suspicious login attempt detected in Splunk logs.",
        "logs": [
            "2025-01-11 17:08:12.007 User 'guest' login attempt from IP 192.168.1.50. Status: Success",
            "2025-01-11 17:09:00.011 User 'guest' login attempt from IP 192.168.1.50. Status: Failed",
            "2025-01-11 17:10:12.500 User 'guest' login attempt from IP 192.168.1.50. Status: Failed",
            "2025-01-11 17:10:30.000 User 'admin' login attempt from IP 192.168.1.100. Status: Success",
            "2025-01-11 17:11:15.320 User 'guest' login attempt from IP 192.168.1.50. Status: Failed"
        ],
        "options": {
            "Block IP 192.168.1.50": "Correct! Multiple failed attempts from the same IP address suggest brute force attack.",
            "Notify user 'guest' about failed attempts": "Incorrect. While informing the user is important, blocking the IP prevents further attacks.",
            "Ignore and monitor for further suspicious activities": "Partially correct. Monitoring is important, but action should be taken after multiple failed attempts."
        },
        "correct": "Block IP 192.168.1.50",
        "explanation": "Blocking the IP prevents the attacker from trying additional login attempts and possibly compromising the system."
    },
    {
        "description": "Network intrusion detected from suspicious traffic pattern.",
        "logs": [
            "2025-01-11 17:13:02.014 Source IP 10.0.0.5, Destination IP 192.168.10.20, Traffic Type: Unknown Protocol",
            "2025-01-11 17:13:30.032 Source IP 10.0.0.5, Destination IP 192.168.10.20, Traffic Type: High volume",
            "2025-01-11 17:14:00.255 Source IP 10.0.0.5, Destination IP 192.168.10.20, Traffic Type: High volume",
            "2025-01-11 17:15:00.290 Source IP 10.0.0.5, Destination IP 192.168.10.20, Traffic Type: Suspicious protocol"
        ],
        "options": {
            "Disconnect the source IP from the network": "Correct! Disconnecting the source prevents further intrusion and potential damage.",
            "Investigate the traffic to determine if it's legitimate": "Incorrect. While investigation is needed, disconnecting the suspicious source is crucial to prevent further threats.",
            "Ignore and monitor for further suspicious traffic": "Partially correct. Monitoring is important, but immediate isolation prevents further damage."
        },
        "correct": "Disconnect the source IP from the network",
        "explanation": "Disconnecting prevents the attacker from exploiting vulnerabilities and stops the flow of suspicious traffic."
    },
    {
        "description": "Suspicious file transfer detected in Splunk logs.",
        "logs": [
            "2025-01-11 17:20:12.140 File transfer initiated by 'admin' to external IP 198.51.100.5",
            "2025-01-11 17:20:40.180 File transfer completed from 'admin' to external IP 198.51.100.5",
            "2025-01-11 17:22:12.350 File transfer initiated by 'employee01' to external IP 198.51.100.5",
            "2025-01-11 17:22:30.310 File transfer completed from 'employee01' to external IP 198.51.100.5"
        ],
        "options": {
            "Investigate the file transfer activity": "Correct! Investigating the transfer will help identify if it's legitimate or part of a data breach.",
            "Notify the users involved and wait for a response": "Incorrect. Immediate action is needed to prevent data loss or a breach, not just notification.",
            "Ignore the activity as it seems normal": "Partially correct. While it's important to monitor, ignoring potential breaches is risky."
        },
        "correct": "Investigate the file transfer activity",
        "explanation": "Investigating the transfer can reveal whether it was a legitimate operation or part of a malicious data exfiltration attempt."
    },
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

        # Logs label
        self.logs_label = QLabel("", self)
        self.logs_label.setAlignment(Qt.AlignLeft)
        self.logs_label.setStyleSheet("font-size: 12px; color: #A9A9A9;")
        self.layout.addWidget(self.logs_label)

        # Buttons for options
        self.buttons = []
        for i in range(3):  # 3 options per scenario
            btn = QPushButton("", self)
            btn.setStyleSheet("background-color: #333366; color: #00FF00; font-size: 14px;")
            btn.clicked.connect(lambda checked, b=i: self.check_response(b))
            self.layout.addWidget(btn)
            self.buttons.append(btn)

        # Feedback label
        self.feedback_label = QLabel("", self)
        self.feedback_label.setAlignment(Qt.AlignCenter)
        self.feedback_label.setStyleSheet("font-size: 14px; color: #FFD700;")
        self.layout.addWidget(self.feedback_label)

        # Explanation label
        self.explanation_label = QLabel("", self)
        self.explanation_label.setAlignment(Qt.AlignCenter)
        self.explanation_label.setStyleSheet("font-size: 12px; color: #A9A9A9;")
        self.layout.addWidget(self.explanation_label)

        # Next incident button
        self.next_button = QPushButton("Next Incident", self)
        self.next_button.setStyleSheet("background-color: #007ACC; color: #FFFFFF; font-size: 14px;")
        self.next_button.setEnabled(False)
        self.next_button.clicked.connect(self.next_scenario)
        self.layout.addWidget(self.next_button)

        self.setLayout(self.layout)
        self.current_scenario_index = 0
        self.correct_answers = 0
        self.wrong_answers = 0

        # Show first scenario
        self.show_scenario()

    def show_scenario(self):
        scenario = scenarios[self.current_scenario_index]
        self.scenario_label.setText(scenario["description"])
        self.logs_label.setText("\n".join(scenario["logs"]))

        # Randomize options
        options = list(scenario["options"].items())
        random.shuffle(options)
        for i, (option, _) in enumerate(options):
            self.buttons[i].setText(option)

        self.correct_answer = scenario["correct"]
        self.explanation = scenario["explanation"]

        # Reset feedback and explanation
        self.feedback_label.setText("")
        self.explanation_label.setText("")
        self.next_button.setEnabled(False)

    def check_response(self, button_index):
        scenario = scenarios[self.current_scenario_index]
        selected_option = self.buttons[button_index].text()
        
        # Check if the selected option is correct
        if selected_option == self.correct_answer:
            self.correct_answers += 1
            self.feedback_label.setText(f"Correct! {self.explanation}")
            self.explanation_label.setText("")
            self.next_button.setEnabled(True)
        else:
            self.wrong_answers += 1
            self.feedback_label.setText(f"Wrong! {scenario['options'][selected_option]}")
            self.explanation_label.setText(f"Correct answer: {self.correct_answer}")
            self.next_button.setEnabled(True)

    def next_scenario(self):
        self.current_scenario_index += 1
        if self.current_scenario_index < len(scenarios):
            self.show_scenario()
        else:
            self.scenario_label.setText("Game Over!")
            self.logs_label.setText(f"Total Correct Answers: {self.correct_answers}")
            self.feedback_label.setText(f"Total Wrong Answers: {self.wrong_answers}")
            self.next_button.setEnabled(False)

# Main function to run the app
def main():
    app = QApplication(sys.argv)
    window = CyberDefenderApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
