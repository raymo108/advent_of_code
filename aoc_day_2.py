with open('input_day_2.txt', 'r') as file:
    rounds = [i for i in file.read().strip().split("\n")]
    

A = "rock"
B = "paper"
C = "scissors"

X = "rock"
Y = "paper"
Z = "scissors"

rock_score = 1
paper_score = 2
scissor_score = 3
lost = 0
draw = 3
win = 6

total_score = []

for letter in rounds:
    if letter == "A X":
        score = draw + rock_score
        total_score.append(score)
    elif letter == "A Y":
        score = win + paper_score
        total_score.append(score)
    elif letter == "A Z":
        score = scissor_score
        total_score.append(score)
    elif letter == "B X":
        score = rock_score
        total_score.append(score)
    elif letter == "B Y":
        score = draw + paper_score
        total_score.append(score)
    elif letter == "B Z":
        score = win + scissor_score
        total_score.append(score)
    elif letter == "C X":
        score = win + rock_score
        total_score.append(score)
    elif letter == "C Y":
        score = paper_score
        total_score.append(score)
    elif letter == "C Z":
        score = draw + scissor_score
        total_score.append(score)

print(total_score)
sum_total_score = sum(total_score)
print(sum_total_score)