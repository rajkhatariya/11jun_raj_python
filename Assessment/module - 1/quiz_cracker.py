
def play_quiz(questions):
    if not questions:
        print("  No questions available to play.")
        return

    score = 0
    total = len(questions)

    print("\n  Welcome to the Quiz!\n")

    for qid, qdata in questions.items():
        print(f"  {qid}")
        print(f"  {qdata['question']}")
        for i, opt in enumerate(qdata['options'], 1):
            print(f"   {i}. {opt}")
        
        try:
            choice = int(input("Enter your answer (1-4): "))
            if 1 <= choice <= 4:
                selected = qdata['options'][choice - 1]
                if selected == qdata['answer']:
                    print("  Correct!\n")
                    score += 1
                else:
                    print(f"  Wrong! Correct Answer: {qdata['answer']}\n")
            else:
                print("  Invalid choice. Skipping question.\n")
        except ValueError:
            print("  Please enter a valid number.\n")

    print("  Quiz Completed!")
    print(f"Your Score: {score} / {total}")
