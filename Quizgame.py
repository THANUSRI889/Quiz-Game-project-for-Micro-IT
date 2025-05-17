

def run_quiz(questions):
    score = 0
    for question in questions:
        print("\n" + question["question"])
        for option in question["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}")
    print(f"\nYour final score: {score} out of {len(questions)}")

quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. Rome", "C. Madrid", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. Mark Twain", "B. Charles Dickens", "C. William Shakespeare", "D. Jane Austen"],
        "answer": "C"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"],
        "answer": "B"
    }
]

if __name__ == "__main__":
    run_quiz(quiz_questions)
