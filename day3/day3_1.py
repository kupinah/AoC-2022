import csv


def sum_items(reader):
    sum = 0

    for line in reader:
        line = line[0]
        half_line_length = int(len(line)/2)
    
        first_half = [line[:half_line_length]][0]
        second_half = [line[half_line_length:]][0]

        same_char = list(set(first_half).intersection(second_half))[0]

        if ord(same_char) <= ord("Z"):
            diff_val = 38
        else:
            diff_val = 96

        sum += ord(same_char)-diff_val

    return sum

if __name__ == "__main__":
    sum = 0

    with open("day3/input_day3.txt", "r+") as f:
        reader = csv.reader(f)
        print(sum_items(reader))