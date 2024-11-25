import json

def load_questions(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def calculate_final_scores(questions):
    final_scores = []
    for question in questions:
        total_score = 0
        for test_case in question.get('test_cases', []):
            total_score += test_case.get('weightage', 0)
        final_scores.append({
            'question_id': question['question']['question_id'],
            'final_score': total_score
        })
    return final_scores

def print_weightage_per_question(questions):
    for question in questions:
        question_id = question['question']['question_id']
        weightage = sum(test_case.get('weightage', 0) for test_case in question.get('test_cases', []))
        print(f"Question ID: {question_id}, Total Weightage: {weightage}")

if __name__ == "__main__":
    questions = load_questions('./question_list.json')  # Update with the correct path
    final_scores = calculate_final_scores(questions)
    print_weightage_per_question(questions)
    print(final_scores)
