import tkinter as tk
from tkinter import messagebox
import random
import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'


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

# Main application class
class CyberDefenderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberDefender")
        self.root.configure(bg="#1E1E2F")  # Dark theme

        self.current_scenario = 0

        # Scenario label with forced update
        self.scenario_label = tk.Label(
            root, text="Scenario will be displayed here.", wraplength=500, fg="#00FF00", bg="#1E1E2F", font=("Courier New", 16, 'bold'), pady=10
        )
        self.scenario_label.pack(pady=20)  # Added more padding for space
        self.root.update()  # Force widget update

        # Buttons for options
        self.buttons = []
        for _ in range(3):  # 3 options per scenario
            btn = tk.Button(
                root, text="", width=40, bg="#333366", fg="#00FF00",
                font=("Courier New", 12), command=lambda b=_: self.check_response(b)
            )
            btn.pack(pady=5)
            self.buttons.append(btn)

        # Next incident button
        self.next_button = tk.Button(
            root, text="Next Incident", state=tk.DISABLED, width=20,
            bg="#007ACC", fg="#FFFFFF", font=("Courier New", 12), command=self.next_scenario
        )
        self.next_button.pack(pady=10)

        # Initialize the first scenario
        self.load_scenario()

    def load_scenario(self):
        # Debugging step to see the current scenario's description
        print(f"Loading scenario: {scenarios[self.current_scenario]['description']}")
        
        scenario = scenarios[self.current_scenario]
        self.scenario_label.config(text=f"Scenario: {scenario['description']}")  # Make sure text is updated here
        
        # Debugging message to ensure the scenario is being loaded
        print(f"Scenario label updated with description: {scenario['description']}")

        # Force update of the root window to refresh the layout
        self.root.update()

        # Update buttons with options
        for idx, (option, feedback) in enumerate(scenario["options"].items()):
            self.buttons[idx].config(text=option, command=lambda o=option: self.check_response(o))
            self.buttons[idx].config(state=tk.NORMAL)

        # Disable the "Next Incident" button until a response is selected
        self.next_button.config(state=tk.DISABLED)

    def check_response(self, selected_option):
        scenario = scenarios[self.current_scenario]
        feedback = scenario["options"][selected_option]

        # Show feedback in messagebox with cyber color theme
        if selected_option == scenario["correct"]:
            messagebox.showinfo("Response", feedback)
        else:
            messagebox.showwarning("Response", feedback)

        # Disable buttons after a response
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)

        # Enable the "Next Incident" button after selecting an option
        self.next_button.config(state=tk.NORMAL)

    def next_scenario(self):
        self.current_scenario += 1
        if self.current_scenario < len(scenarios):
            self.load_scenario()
        else:
            messagebox.showinfo("Game Over", "You have completed all incidents!")
            self.root.quit()


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = CyberDefenderApp(root)
    root.mainloop()
