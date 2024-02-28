import random

class QuizGame:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Berlin", "Madrid", "Paris", "Rome"],
                "correct_answer": "Paris"
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Leo Tolstoy"],
                "correct_answer": "William Shakespeare"
            },
            {
                "question": "The largest planet in our solar system is?",
                "options": ["Earth", "Jupiter", "Mars", "Venus"],
                "correct_answer": "Jupiter"
            },
            {
                "question": "What is the capital of Japan?",
                "options": ["Beijing", "Seoul", "Tokyo", "Bangkok"],
                "correct_answer": "Tokyo"
            }
            # Add more questions as needed
        ]

        self.score = 0

    def welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("Answer each question and see how well you know the topic.")

    def display_question(self, question):
        print("\n" + question["question"])
        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")

    def evaluate_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")

    def play_game(self):
        self.welcome_message()

        random.shuffle(self.questions)  # Shuffle questions for variety

        for question in self.questions:
            self.display_question(question)
            user_answer = input("Your answer (enter the number or type your answer): ")

            if user_answer.isdigit():
                user_answer = question["options"][int(user_answer) - 1]

            self.evaluate_answer(user_answer, question["correct_answer"])

        print(f"\nYour final score: {self.score}/{len(self.questions)}")
        print("Thanks for playing!")

    def play_again(self):
        return input("Do you want to play again? (yes/no): ").lower() == "yes"

if __name__ == "__main__":
    game = QuizGame()

    while True:
        game.play_game()

        if not game.play_again():
            break
