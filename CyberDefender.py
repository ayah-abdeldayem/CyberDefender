import tkinter as tk
from tkinter import messagebox
import random
import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

# Define scenarios with a more technical twist
scenarios = [
    {
        "description": "Suspicious login detected from a foreign IP address.",
        "logs": [
            "2025-01-11 12:32:47 [INFO] User 'jdoe' logged in from IP 192.168.100.200.",
            "2025-01-11 12:32:48 [WARNING] Foreign IP detected: 186.45.67.89.",
            "2025-01-11 12:32:50 [ALERT] Possible unauthorized access attempt."
        ],
        "options": {
            "Block the user's account": "Correct! Blocking prevents unauthorized access.",
            "Ignore and monitor the situation": "Incorrect. Monitoring allows the attacker more time.",
            "Notify the user to verify the login": "Partially correct. Verifying adds a layer of security, but blocking is safer."
        },
        "correct": "Block the user's account"
    },
    {
        "description": "Malware detected on an employee's computer.",
        "logs": [
            "2025-01-11 14:04:55 [INFO] Malware signature 'Trojan.Generic' detected.",
            "2025-01-11 14:04:58 [ALERT] Malware execution detected: process 'bad.exe' running.",
            "2025-01-11 14:05:00 [INFO] Network traffic from compromised machine to external IP."
        ],
        "options": {
            "Disconnect the computer from the network": "Correct! This prevents further spread.",
            "Run a full antivirus scan": "Incorrect. Scanning delays immediate containment.",
            "Notify all employees to check their devices": "Partially correct. It's useful, but immediate isolation is better."
        },
        "correct": "Disconnect the computer from the network"
    },
    {
        "description": "Unusual traffic spike detected from a server.",
        "logs": [
            "2025-01-11 16:12:10 [INFO] Incoming traffic spike detected on server 'srv-02'.",
            "2025-01-11 16:12:12 [WARNING] Abnormal traffic from IP 145.32.50.77.",
            "2025-01-11 16:12:13 [ALERT] Possible DDoS attack detected."
        ],
        "options": {
            "Analyze the traffic and block suspicious IPs": "Correct! Blocking malicious IPs reduces risk.",
            "Reboot the server": "Incorrect. Rebooting doesn't address the root cause.",
            "Ignore and monitor the traffic": "Incorrect. Monitoring delays containment."
        },
        "correct": "Analyze the traffic and block suspicious IPs"
    },
    {
        "description": "Employee reported a phishing email.",
        "logs": [
            "2025-01-11 11:45:00 [INFO] Phishing email detected in 'jdoe' inbox.",
            "2025-01-11 11:45:02 [ALERT] Malicious URL identified: 'http://example.phishing.com'.",
            "2025-01-11 11:45:05 [WARNING] User clicked on phishing link."
        ],
        "options": {
            "Warn all employees about the phishing attempt": "Correct! Awareness prevents further clicks.",
            "Delete the email and move on": "Incorrect. This doesn't inform others.",
            "Report the phishing email to authorities": "Partially correct. Reporting is good but not immediate."
        },
        "correct": "Warn all employees about the phishing attempt"
    }
]

# Main application class
class CyberDefenderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberDefender")
        self.root.configure(bg="#0A0A1B")  # Dark cyber theme

        self.current_scenario = 0
        self.time_limit = 30  # Time limit for each scenario in seconds
        self.timer = None

        # Scenario label
        self.scenario_label = tk.Label(
            root, text="", wraplength=500, fg="#A8FF40", bg="#0A0A1B", font=("Courier New", 14), pady=10
        )
        self.scenario_label.pack()

        # Logs display area
        self.logs_text = tk.Label(
            root, text="", wraplength=500, fg="#66FF66", bg="#0A0A1B", font=("Courier New", 12), padx=10, pady=10
        )
        self.logs_text.pack()

        # Buttons for options
        self.buttons = []
        for _ in range(3):  # 3 options per scenario
            btn = tk.Button(
                root, text="", width=40, bg="#3B3B4F", fg="#FFFFFF",
                font=("Courier New", 12), command=lambda b=_: self.check_response(b)
            )
            btn.pack(pady=5)
            self.buttons.append(btn)

        # Timer label
        self.timer_label = tk.Label(
            root, text=f"Time Left: {self.time_limit}", fg="#FF5733", bg="#0A0A1B", font=("Courier New", 12)
        )
        self.timer_label.pack(pady=5)

        # Next incident button
        self.next_button = tk.Button(
            root, text="Next Incident", state=tk.DISABLED, width=20,
            bg="#007ACC", fg="#FFFFFF", font=("Courier New", 12), command=self.next_scenario
        )
        self.next_button.pack(pady=10)

        # Initialize the first scenario
        self.load_scenario()

    def load_scenario(self):
        scenario = scenarios[self.current_scenario]
        self.scenario_label.config(text=f"Scenario: {scenario['description']}")
        self.logs_text.config(text="\n".join(scenario['logs']))

        for idx, (option, feedback) in enumerate(scenario["options"].items()):
            self.buttons[idx].config(text=option, command=lambda o=option: self.check_response(o))
            self.buttons[idx].config(state=tk.NORMAL)

        self.next_button.config(state=tk.DISABLED)

        # Reset the timer
        self.start_timer()

    def check_response(self, selected_option):
        scenario = scenarios[self.current_scenario]
        feedback = scenario["options"][selected_option]

        # Show feedback
        if selected_option == scenario["correct"]:
            messagebox.showinfo("Response", feedback)
        else:
            messagebox.showwarning("Response", feedback)

        # Disable buttons after a response
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)

        self.next_button.config(state=tk.NORMAL)

    def next_scenario(self):
        self.current_scenario += 1
        if self.current_scenario < len(scenarios):
            self.load_scenario()
        else:
            messagebox.showinfo("Game Over", "You have completed all incidents!")
            self.root.quit()

    def start_timer(self):
        self.time_left = self.time_limit
        self.timer_label.config(text=f"Time Left: {self.time_left}")
        self.timer = self.root.after(1000, self.update_timer)

    def update_timer(self):
        self.time_left -= 1
        self.timer_label.config(text=f"Time Left: {self.time_left}")

        if self.time_left <= 0:
            messagebox.showwarning("Time's Up", "Time's up! Moving to next incident.")
            self.next_scenario()
        else:
            self.timer = self.root.after(1000, self.update_timer)


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = CyberDefenderApp(root)
    root.mainloop()
