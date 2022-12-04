import csv
from os.path import join
from pathlib import Path


def get_overlaps(lines):
    num_of_overlaps = 0
    for line in lines:
        pair_1 = line[0].split("-")
        pair_2 = line[1].split("-")

        if (int(pair_1[0]) <= int(pair_2[0])) and (int(pair_1[1]) >= int(pair_2[1])):
            num_of_overlaps += 1
            continue

        if (int(pair_2[0]) <= int(pair_1[0])) and (int(pair_2[1]) >= int(pair_1[1])):
            num_of_overlaps += 1

    return num_of_overlaps

if __name__ == "__main__":
    current_file_parent = Path(__file__).absolute().parent
    input_path = join(current_file_parent, "input_day4.txt")
   
    with open(input_path, "r+") as f:
        reader = csv.reader(f, delimiter=",")
        print(get_overlaps(reader))