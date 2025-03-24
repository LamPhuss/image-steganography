import re

# Load the data from the text file
with open("mobile-final-out-sorted.txt", "r") as f:
    lines = f.readlines()
# Split the data into questions and answers
questions = []
current_question = ""
current_answer = ""

for line in lines:
    line = line.strip()
    if line.startswith("#"):
        if current_question:
            questions.append([current_question, current_answer])
            current_answer = "" # Reset answer after appending
        current_question = line[1:].strip()  # Capture question
    elif line:  # Only append non-empty lines to the answer
        current_answer += line + " "

if current_question:
    questions.append([current_question, current_answer])
# Sort the questions based on the answer text
questions.sort(key=lambda x: re.sub(r'[^a-zA-Z0-9]', '', x[1].lower()))

# Write the sorted questions back to the file
with open("your_file_sorted.txt", "w") as f:
    for question, answer in questions:
        f.write("# " + question + "\n")
        f.write(answer.strip() + "\n")

print("File sorted successfully!")