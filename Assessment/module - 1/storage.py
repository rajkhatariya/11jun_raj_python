import json
import os

FILE_NAME = "questions.json"

def load_questions():
    if not os.path.exists(FILE_NAME):
        return {}  
    
    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {} 

def save_questions(questions):
    with open(FILE_NAME, "w") as file:
        json.dump(questions, file, indent=4)
