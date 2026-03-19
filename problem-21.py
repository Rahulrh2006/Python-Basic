#split function
data = "What is the capital of France? Paris"
try:
    question, answer = data.split('?', 1) 
    print(f"Question: {question.strip()}")
    print(f"Answer: {answer.strip()}")
except ValueError:
    print("The string format is incorrect, could not split into two parts.")

