import csv


def get_score(reader):
    
    score = 0
    # X / A - rock => +1
    # Y / B - paper => +2 
    # Z / C - scissors => +3

    for opponent, me in reader:
        if me == "X":
            score+=1

            if opponent == "A":
                score += 3

            elif opponent == "C":
                score += 6 

        elif me == "Y":
            score += 2

            if opponent == "A":
                score += 6

            elif opponent == "B":
                score += 3

        else:

            score += 3

            if opponent == "B":
                score += 6

            elif opponent == "C":
                score += 3
    
    return score
if __name__ == "__main__":
    path = "input_day2.txt"
    with open(path, "r+") as f:
        reader = csv.reader(f, delimiter=" ")

        score = get_score(reader)
    print(f"My score is {score}.")

