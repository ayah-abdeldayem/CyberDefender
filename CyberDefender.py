import random
from tkinter import *
from tkinter import messagebox
from faker import Faker

# Initialize Faker for realistic data
faker = Faker()

# Predefined scenarios with full incident details
INCIDENTS = [
    {
        "name": "Brute Force Attack",
        "log": lambda: f"[ALERT] {faker.date_time()} Multiple failed login attempts detected from IP {faker.ipv4()}",
        "questions": [
            {
                "question": "What should you do first?",
                "options": ["Block the IP", "Investigate the user account", "Ignore the alert"],
                "correct": "Block the IP",
                "feedback": "Blocking the IP prevents further unauthorized attempts."
            },
            {
                "question": "What logs should you check next?",
                "options": ["Authentication logs", "Network traffic logs", "DNS logs"],
                "correct": "Authentication logs",
                "feedback": "Authentication logs will show login attempts and help identify the source."
            },
            {
                "question": "What is a good post-incident action?",
                "options": ["Reset passwords", "Disable all accounts", "Do nothing"],
                "correct": "Reset passwords",
                "feedback": "Resetting passwords ensures compromised credentials can't be reused."
            },
        ],
    },
    {
        "name": "Phishing Email",
        "log": lambda: f"[ALERT] {faker.date_time()} Suspicious email detected: '{faker.text(max_nb_chars=50)}'",
        "questions": [
            {
                "question": "What should you do first?",
                "options": ["Quarantine the email", "Notify all employees", "Delete the email"],
                "correct": "Quarantine the email",
                "feedback": "Quarantining the email prevents users from interacting with malicious content."
            },
            {
                "question": "What should you analyze in the email?",
                "options": ["Links and attachments", "Font style", "Sender's job title"],
                "correct": "Links and attachments",
                "feedback": "Analyzing links and attachments helps identify phishing indicators."
            },
            {
                "question": "What is a good post-incident action?",
                "options": ["Conduct employee training", "Send an apology email", "Ignore it"],
                "correct": "Conduct employee training",
                "feedback": "Training employees reduces the risk of successful phishing attacks."
            },
        ],
    },
    # Add more incidents as needed
]

# Initialize score
score = 0
current_question = 0
selected_incident = None

# Start game
def start_game():
    global selected_incident, current_question, score
    score = 0
    current_question = 0
    selected_incident = random.choice(INCIDENTS)
    display_log(selected_incident["log"]())

# Display incident log
def display_log(log):
    for widget in frame.winfo_children():
        widget.destroy()
    Label(frame, text="Incident Log:", font=("Arial", 16, "bold"), fg="#00FFFF", bg="#1E1E1E").pack(pady=10)
    Label(frame, text=log, font=("Arial", 12), wraplength=400, fg="white", bg="#1E1E1E").pack(pady=10)
    Button(frame, text="Investigate", command=next_question, font=("Arial", 12), bg="#2A2A2A", fg="#00FFFF", relief=GROOVE).pack(pady=10)

# Display the next question
def next_question():
    global current_question
    for widget in frame.winfo_children():
        widget.destroy()

    if current_question >= len(selected_incident["questions"]):
        end_game()
        return

    question_data = selected_incident["questions"][current_question]
    Label(frame, text=question_data["question"], font=("Arial", 14, "bold"), fg="#00FFFF", bg="#1E1E1E").pack(pady=10)
    for i, option in enumerate(question_data["options"]):
        Button(
            frame,
            text=option,
            font=("Arial", 12),
            bg="#2A2A2A",
            fg="white",
            relief=GROOVE,
            command=lambda opt=option: check_answer(opt, question_data),
        ).pack(pady=5)

# Check the user's answer
def check_answer(selected_option, question_data):
    global score, current_question
    if selected_option == question_data["correct"]:
        messagebox.showinfo("Correct!", question_data["feedback"])
        score += 1
    else:
        messagebox.showwarning("Incorrect", f"Correct answer: {question_data['correct']}\n{question_data['feedback']}")

    current_question += 1
    next_question()

# End the game and show results
def end_game():
    for widget in frame.winfo_children():
        widget.destroy()

    Label(frame, text="Game Over!", font=("Arial", 18, "bold"), fg="#00FFFF", bg="#1E1E1E").pack(pady=10)
    Label(frame, text=f"Final Score: {score}/{len(selected_incident['questions'])}", font=("Arial", 14), fg="white", bg="#1E1E1E").pack(pady=10)
    Button(frame, text="Play Again", command=start_game, font=("Arial", 12), bg="#2A2A2A", fg="#00FFFF", relief=GROOVE).pack(pady=10)
    Button(frame, text="Exit", command=root.quit, font=("Arial", 12), bg="#2A2A2A", fg="white", relief=GROOVE).pack(pady=10)

# Set up the Tkinter interface
root = Tk()
root.title("CyberDefender")
root.geometry("500x400")
root.configure(bg="#1E1E1E")

frame = Frame(root, bg="#1E1E1E")
frame.pack(expand=True, fill=BOTH)

start_game()

root.mainloop()
