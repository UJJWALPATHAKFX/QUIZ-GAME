#quiz game for legal ages


questions = ("what is the correct age to become legal?: ",
             "What is the correct age to drink?: ",
             "What is the correct age to smoke?: ",
             "What is the correct age to drive?: ",
             "How many states are there in our country?: ")
options = (("A. 18", "B. 12", "C. 21", "D. 11"),
           ("A. 22", "B. 33", "C. 21", "D. 24"),
           ("A. 17", "B. 14", "C. 16", "D. 18"),
           ("A. 18", "B. 15", "C. 34", "D. 42"),
           ("A. 28", "B. 34", "C. 29", "D. 30"))
answers = ("A", "A", "D", "A", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter the correct option from above: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!!!")
    else:
        print("INCORRECT!!!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
print("-----------------------------------")
print("-----------RESULT!!------------")
print("-----------------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = (score / len(questions) * 100)
print(f"Your total Score is {score}%")
if score < 2:
    print("BAD LUCK😬😬😬😬!!")
else:
    print("Congratulations!!!!🥳🥳🥳🥳")