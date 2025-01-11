import tkinter as tk
from tkinter import ttk

# Sample incidents
incidents = [
    {
        "description": "🚨 Incident 1: Suspicious login detected! A user has logged in from an unusual location. What would you do?",
        "options": [
            ("Block the user's account", "Good choice! The account has been blocked."),
            ("Ignore and monitor the situation", "The attacker gained access. Better luck next time!"),
            ("Notify the user to verify the login", "Great job! The user confirmed the login was unauthorized."),
        ]
    },
    {
        "description": "🚨 Incident 2: A phishing email has been reported by an employee. What is your next step?",
        "options": [
            ("Delete the email", "The email is deleted, but no further action was taken."),
            ("Investigate the email headers and attachments", "Excellent! You identified the malicious link and blocked it."),
            ("Send a company-wide alert", "Smart! Everyone has been warned about the phishing attempt."),
        ]
    },
    {
        "description": "🚨 Incident 3: Malware detected on a workstation. Immediate action is required. What will you do?",
        "options": [
            ("Disconnect the workstation from the network", "Correct! The malware was contained."),
            ("Run antivirus on the workstation", "Too slow! The malware spread before being detected."),
            ("Reboot the system", "Not ideal! The malware persisted after reboot."),
        ]
    },
    {
        "description": "🚨 Incident 4: Unusual outbound traffic detected from a server. What should you do first?",
        "options": [
            ("Inspect network traffic logs", "Great choice! You identified the suspicious IPs and blocked them."),
            ("Shut down the server immediately", "Effective, but it caused downtime for legitimate users."),
            ("Notify the server administrator", "Good step, but the delay allowed the attacker to exfiltrate data."),
        ]
    }
]

class CyberDefenderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberDefender")
        self.root.geometry("800x600")
        self.root.configure(bg="#1e1e2e")

        self.current_incident = 0

        # Title Label
        self.title_label = tk.Label(
            root, text="🛡️ CyberDefender Incident Response Simulator",
            font=("Helvetica", 18, "bold"), fg="#00aaff", bg="#1e1e2e"
        )
        self.title_label.pack(pady=20)

        # Incident Description
        self.incident_label = tk.Label(
            root, text="", wraplength=700, justify="left",
            font=("Helvetica", 14), fg="white", bg="#1e1e2e"
        )
        self.incident_label.pack(pady=10)

        # Options Frame
        self.options_frame = tk.Frame(root, bg="#1e1e2e")
        self.options_frame.pack(pady=20)

        # Feedback Label
        self.feedback_label = tk.Label(
            root, text="", font=("Helvetica", 14, "italic"),
            fg="#ffaa00", bg="#1e1e2e", wraplength=700, justify="left"
        )
        self.feedback_label.pack(pady=10)

        # Navigation Buttons
        self.next_button = tk.Button(
            root, text="Next Incident", command=self.next_incident,
            state=tk.DISABLED, bg="#333344", fg="white", font=("Helvetica", 12)
        )
        self.next_button.pack(pady=10)

        # Load the first incident
        self.display_incident()

    def display_incident(self):
        incident = incidents[self.current_incident]
        self.incident_label.config(text=incident["description"])
        self.feedback_label.config(text="")

        # Clear previous options
        for widget in self.options_frame.winfo_children():
            widget.destroy()

        # Display options
        for text, feedback in incident["options"]:
            button = tk.Button(
                self.options_frame, text=text, wraplength=600, justify="left",
                command=lambda fb=feedback: self.display_feedback(fb),
                bg="#333344", fg="white", font=("Helvetica", 12)
            )
            button.pack(fill="x", pady=5, padx=10)

    def display_feedback(self, feedback):
        self.feedback_label.config(text=feedback)
        self.next_button.config(state=tk.NORMAL)

    def next_incident(self):
        self.current_incident += 1
        if self.current_incident < len(incidents):
            self.display_incident()
            self.next_button.config(state=tk.DISABLED)
        else:
            self.incident_label.config(text="🎉 Congratulations! You have completed all incidents.")
            self.options_frame.destroy()
            self.feedback_label.config(text="")
            self.next_button.config(state=tk.DISABLED)

# Run the app
root = tk.Tk()
app = CyberDefenderApp(root)
root.mainloop()
