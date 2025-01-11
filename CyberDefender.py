import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QGraphicsView, QGraphicsScene
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

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
    # Add additional scenarios as needed
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

        # Add graphics view for confetti
        self.graphics_view = QGraphicsView(self)
        self.graphics_view.setStyleSheet("background-color: transparent;")
        self.graphics_view.setGeometry(0, 0, 800, 600)
        self.graphics_view.setVisible(False)
        self.layout.addWidget(self.graphics_view)

        # Set up the scene and confetti
        self.scene = QGraphicsScene()
        self.graphics_view.setScene(self.scene)
        self.confetti_particles = []

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
            self.end_game()

    def end_game(self):
        self.scenario_label.setText("Game Over!")
        self.logs_label.setText(f"Total Correct Answers: {self.correct_answers}")
        self.feedback_label.setText(f"Total Wrong Answers: {self.wrong_answers}")
        self.next_button.setEnabled(False)

        # Hide buttons and show hacker image and confetti
        for button in self.buttons:
            button.setVisible(False)

        # Display the hacker image
        hacker_image = QLabel(self)
        hacker_pixmap = QPixmap("hacker_image.png")  # Make sure to add a hacker image in the directory
        hacker_image.setPixmap(hacker_pixmap.scaled(400, 400, Qt.KeepAspectRatio))
        hacker_image.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(hacker_image)

        # Show confetti animation
        self.show_confetti()

    def show_confetti(self):
        # Simple confetti effect using circles
        for _ in range(100):
            particle = self.scene.addEllipse(
                random.randint(0, 800), random.randint(0, 600),
                random.randint(5, 15), random.randint(5, 15),
                brush=Qt.green
            )
            self.confetti_particles.append(particle)
        
        # Start confetti animation
        self.animate_confetti()

    def animate_confetti(self):
        # Simulate a simple movement for the confetti particles
        for particle in self.confetti_particles:
            x_move = random.randint(-5, 5)
            y_move = random.randint(-5, 5)
            particle.setPos(particle.x() + x_move, particle.y() + y_move)

        # Continue animation every 50 milliseconds
        QTimer.singleShot(50, self.animate_confetti)

# Main function to run the app
def main():
    app = QApplication(sys.argv)
    window = CyberDefenderApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
