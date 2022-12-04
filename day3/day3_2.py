import csv


def find_common(group):
    common_char = list(set(group[0][0]) & set(group[1][0]) & set(group[2][0]))[0]
    return common_char
    
def sum_items(reader):
    sum = 0
    group = []
    for num, line in enumerate(reader):
        group.append(line)

        if num % 3 == 2:
            common_char = find_common(group)

            if ord(common_char) <= ord("Z"):
                diff_val = 38
            else:
                diff_val = 96

            sum += ord(common_char)-diff_val

            group = []

    return sum
    


if __name__ == "__main__":
    sum = 0

    with open("day3/input_day3.txt", "r+") as f:
        reader = csv.reader(f)
        print(sum_items(reader))