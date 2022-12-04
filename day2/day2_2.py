import csv


def get_score(reader):
    score = 0
    # X - lose
    # Y - draw
    # Z - win

    # A - rock => +1
    # B - paper => +2 
    # C - scissors => +3

    for opponent, me in reader:
        if me == "X":
            if opponent == "A":
                score += 3
            elif opponent == "B":
                score += 1
            else:
                score += 2 

        elif me == "Y":
            score += 3
            if opponent == "A":
                score += 1
            elif opponent == "B":
                score += 2
            else:
                score += 3

        else:
            score += 6
            if opponent == "A":
                score += 2
            elif opponent == "B":
                score += 3
            else:
                score += 1 
    
    return score
if __name__ == "__main__":
    path = "input_day2.txt"
    with open(path, "r+") as f:
        reader = csv.reader(f, delimiter=" ")

        score = get_score(reader)
    print(f"My score is {score}.")

