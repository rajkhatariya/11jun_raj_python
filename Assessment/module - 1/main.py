from quiz_master import add_question, view_questions, delete_question
from quiz_cracker import play_quiz
from storage import load_questions, save_questions

def main_menu():
    while True:
        print("\n\t\t\t\t===   Quiz Game Main Menu ===")
        print("\n\t\t\t\t\t1. Quiz Master")
        print("\t\t\t\t\t2. Quiz Cracker")
        print("\t\t\t\t\t3. Exit Game")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == '1':
            quiz_master_menu()
        elif choice == '2':
            questions = load_questions()
            play_quiz(questions)
        elif choice == '3':
            print("  Exiting... Thank you for playing!")
            break
        else:
            print(" Invalid input. Try again.")


def quiz_master_menu():
    questions = load_questions()

    while True:
        print("\n---   Quiz Master Menu ---")
        print("1. Add Question")
        print("2. View All Questions")
        print("3. Delete a Question")
        print("4. Exit to Main Menu")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_question(questions)
        elif choice == '2':
            view_questions(questions)
        elif choice == '3':
            delete_question(questions)
        elif choice == '4':
            save_questions(questions)
            print("  Questions saved. Returning to main menu...")
            break
        else:
            print(" Invalid input. Please enter 1-4.")


main_menu()
