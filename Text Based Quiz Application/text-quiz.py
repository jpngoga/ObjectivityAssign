
import random

def quiz(questions):
    score = 0
    for question in questions:
        print(question['question'])
        for i, choice in enumerate(question['choices']):
            print(f"{i + 1}. {choice}")
        answer = int(input("Enter your answer: "))
        if question['choices'][answer - 1] == question['answer']:
            score += 10
            print("Correct!")
        else:
            print("Incorrect.")
    print(f"Final score: {score}/{len(questions)*10}")

questions = [
    {
        'question': 'Which of this in not a programming Language?',
        'choices': ['React Js', 'C', 'PHP', 'Python'],
        'answer': 'React Js'
    },
    {
        'question': 'What is the capital of France?',
        'choices': ['Paris', 'London', 'Berlin', 'Barcelona'],
        'answer': 'Paris'
    },
    {
        'question': 'What is the Os that used in Apple?',
        'choices': ['Linux', 'DOS', 'MAC OS', 'Windows'],
        'answer': 'Paris'
    },
    {
        'question': 'What is the largest planet in our solar system?',
        'choices': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
        'answer': 'Jupiter'
    },

    {
        'question': 'What is the President of Rwanda?',
        'choices': ['Kayibanda', 'Pierre Mugisha', 'Kagame Paul', 'Nsengiyaremye Joel'],
        'answer': 'Kagame Paul'
    },
]

random.shuffle(questions)
quiz(questions)