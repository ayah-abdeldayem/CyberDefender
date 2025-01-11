import random
import time
from faker import Faker
faker = Faker()
#initialize scenarios and reponses
INCIDENTS = [
    {
        "name": "Brute Force Attack",
        "log": lambda: f"[ALERT] {faker.date_time()} Repeated failed login attempts from IP {faker.ipv4()}.",
        "correct_action": "Block IP",
        "explanation": "Blocking the IP prevents further unauthorized attempts."
    },
    {
        "name": "Phishing Email",
        "log": lambda: f"[ALERT] {faker.date_time()} Suspicious email detected: '{faker.text(max_nb_chars=50)}'.",
        "correct_action": "Quarantine Email",
        "explanation": "Quarantining the email prevents users from clicking malicious links."
    },
    {
        "name": "Data Exfiltration",
        "log": lambda: f"[WARNING] {faker.date_time()} Large outbound traffic detected from {faker.domain_name()}.",
        "correct_action": "Investigate Server",
        "explanation": "Investigating the server helps identify the source of the anomaly."
    },
    {
        "name": "Malware Detection",
        "log": lambda: f"[ALERT] {faker.date_time()} Malware found in file {faker.file_name(extension='exe')}.",
        "correct_action": "Quarantine File",
        "explanation": "Quarantining the file prevents malware from spreading."
    },
]
# Helper function to display a scenario
def generate_incident():
    incident = random.choice(INCIDENTS)
    log = incident["log"]()
    return incident, log

# Game logic
def play_game():
    print("Welcome to the Cybersecurity Incident Simulation Game!")
    print("Analyze the logs and respond appropriately.")
    print("-" * 50)

    score = 0
    for _ in range(5):  # Play 5 rounds
        incident, log = generate_incident()
        print(f"\nIncident Log: {log}")
        print("Choose your action:")
        options = ["Block IP", "Quarantine Email", "Investigate Server", "Quarantine File"]
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        try:
            user_choice = int(input("Enter the number of your action: "))
            chosen_action = options[user_choice - 1]
        except (ValueError, IndexError):
            print("Invalid choice! Moving to the next incident.")
            continue

        if chosen_action == incident["correct_action"]:
            print("✅ Correct!")
            print(incident["explanation"])
            score += 1
        else:
            print(f"❌ Incorrect! The correct action was: {incident['correct_action']}")
            print(incident["explanation"])

        time.sleep(1)

    print("\nGame Over!")
    print(f"Your final score: {score}/5")
    if score == 5:
        print("🎉 Excellent work! You're a cybersecurity expert!")
    elif score >= 3:
        print("👍 Good job! Keep practicing!")
    else:
        print("🛠️ Keep learning and improving!")

        # Run the game
if __name__ == "__main__":
    play_game()