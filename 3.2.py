import json
import csv

def load_quiz_data(filename):
  """
  Loads quiz data (questions and answers) from a file.

  Args:
      filename: The path to the quiz data file (text, JSON, or CSV).

  Returns:
      A list of dictionaries, where each dictionary represents a question-answer pair.
  """
  with open(filename, 'r') as f:
    if filename.endswith('.json'):
      data = json.load(f)
    elif filename.endswith('.csv'):
      reader = csv.reader(f)
      data = list(reader)
    else:
      # Handle text file format (assuming each line is a question-answer pair separated by a colon)
      data = [line.strip().split(':') for line in f.readlines()]
  return data

def ask_question(question):
  """
  Asks the user a question and returns their answer.
  """
  answer = input(question + " ")
  return answer.strip()

def grade_quiz(questions, answers):
  """
  Grades the quiz and calculates the score.

  Args:
      questions: A list of questions.
      answers: A list of user answers.

  Returns:
      The user's score (number of correct answers).
  """
  score = 0
  for i, (question, answer) in enumerate(zip(questions, answers)):
    if answer.lower() == question['answer'].lower():
      score += 1
  return score

def save_results(username, score, filename):
  """
  Saves the user's name and score to a file (CSV or JSON).

  Args:
      username: The user's name.
      score: The user's quiz score.
      filename: The path to the results file (CSV or JSON).
  """
  data = {'username': username, 'score': score}
  with open(filename, 'a') as f:
    if filename.endswith('.json'):
      json.dump(data, f, indent=2)
    else:
      writer = csv.writer(f)
      writer.writerow([username, score])

def main():
  # Get quiz data filename
  filename = input("Enter the quiz data file (text, JSON, or CSV): ")

  # Load quiz data
  quiz_data = load_quiz_data(filename)

  # Get user name
  username = input("Enter your name: ")

  # Initialize empty lists for questions and answers
  questions = []
  answers = []

  # Ask questions and store answers
  for question in quiz_data:
    if isinstance(question, dict):
      questions.append(question['question'])
    else:
      questions.append(question[0])
    answer = ask_question(question)
    answers.append(answer)

  # Calculate score
  score = grade_quiz(questions, answers)

  # Display results
  print(f"Hi {username}, your score is {score} out of {len(questions)}.")

  # Save results (optional)
  result_filename = input("Enter a filename to save your results (optional, CSV or JSON): ")
  if result_filename:
    save_results(username, score, result_filename)

if __name__ == "__main__":
  main()
