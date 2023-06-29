#!/usr/bin/env python3

animals_intrus = [
    ["whale", "code", "polar bear", "tuna"],
    ["jaguar", "lion", "tiger", "peacock"],
    ["gorilla", "orangutan", "panda", "chimpanzee"],
    ["anaconda", "boa", "rattlesnake", "tarantula"]
]

good_answer = 0
incorrect_answer = 0
your_answer = []

# print(animals)
# print(animals[0])
# print(animals[0][1])

for list in animals_intrus:
    print(list)
    answer = input("What animal does not fit here?\n ").lower()
    your_answer.append(answer)
    print("-"*15)

if your_answer[0] == animals_intrus[0][2]:
    good_answer += 1
else:
    incorrect_answer += 1

if your_answer[1] == animals_intrus[1][3]:
    good_answer += 1
else:
    incorrect_answer += 1

if your_answer[2] == animals_intrus[2][2]:
    good_answer += 1
else:
    incorrect_answer += 1

if your_answer[3] == animals_intrus[3][3]:
    good_answer += 1
else:
    incorrect_answer += 1


# print(good_answer)

# print(your_answer)
# total_questions = good_answers + incorrect_answers
total_questions = len(animals_intrus)
percentage = round((good_answer / total_questions * 100), 0)

if percentage >= 80:
    grade = "grade A"
elif percentage >= 70:
    grade = "grade B"
elif percentage >= 60:
    grade = "grade C"
elif percentage >= 50:
    grade = "grade D"
elif percentage >= 40:
    grade = "grade E"
else:
    grade = "grade F"

print(
    f"You've got a total of {good_answer} correct answers out of {total_questions}\n {percentage} % of good answers means {grade}")
