import random

# Sample quiz questions and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "choices": ["London", "Madrid", "Paris", "Berlin"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Earth", "Mars", "Venus", "Jupiter"],
        "correct_answer": "Mars"
    },
    {
        "question": "When did India get Independence?",
        "choices": ["1940", "1800", "1947", "1950"],
        "correct_answer": "1947"  
    },
]

def play_quiz():
    score = 0

    print("Welcome to the Quiz Game!")
    print("Answer the following questions:")

    random.shuffle(quiz_data)  # Shuffle the questions for variety

    for question_data in quiz_data:
        print("\n" + question_data["question"])
        for i, choice in enumerate(question_data["choices"], 1):
            print(f"{i}. {choice}")

        user_answer = input("Your choice: ")

        if user_answer.lower() == question_data["correct_answer"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {question_data['correct_answer']}")

    print(f"\nYour Final Score: {score}/{len(quiz_data)}")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_quiz()

play_quiz()
