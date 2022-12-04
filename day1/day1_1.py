def load_input(path):
    elves = []
    elf_ix = 0
    max_value = -1
    with open(path, "r+") as f:
        elves.append(0)
        while True:
            line = f.readline()

            if not line:
                return max_value

            elif line == "\n":
                if elves[elf_ix] > max_value:
                    max_value = elves[elf_ix]

                elf_ix += 1
                elves.append(0)

            else:
                elves[elf_ix] += int(line)



if __name__ == "__main__":
    path = "input_day1.txt"
    print(f"Maximum number of calories is {load_input(path)}.")