import random
import time
from faker import Faker

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
