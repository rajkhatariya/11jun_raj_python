
def add_question(questions):
    try:
        qid = input("Enter question ID (e.g. Q1): ").strip().upper()
        if qid in questions:
            print("  Question ID already exists.")
            return

        question = input("Enter the question: ").strip()
        options = []
        for i in range(4):
            opt = input(f"Enter option {i+1}: ").strip()
            options.append(opt)

        answer = input("Enter the correct answer: ").strip()

        if answer not in options:
            print("  Answer must be one of the options.")
            return

        questions[qid] = {
            "question": question,
            "options": options,
            "answer": answer
        }

        print("  Question added successfully.")
    
    except Exception as e:
        print(f"  Error: {e}")


def view_questions(questions):
    if not questions:
        print("  No questions available.")
        return
    
    for qid, qdata in questions.items():
        print(f"\n  {qid}")
        print(f"  {qdata['question']}")
        for i, opt in enumerate(qdata['options'], 1):
            print(f"   {i}. {opt}")
        print(f"  Answer: {qdata['answer']}")


def delete_question(questions):
    qid = input("Enter Question ID to delete: ").strip().upper()
    if qid not in questions:
        print("  Question ID not found.")
        return

    confirm = input(f"Are you sure you want to delete {qid}? (Y/N): ").strip().lower()
    if confirm == 'y':
        del questions[qid]
        print("  Question deleted successfully.")
    else:
        print("  Deletion cancelled.")
