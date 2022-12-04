def load_input(path):
    elves = []
    elf_ix = 0
    top_values = [-1, -1, -1]
    with open(path, "r+") as f:
        elves.append(0)
        while True:
            line = f.readline()

            if not line:
                print(top_values)
                return sum(top_values)

            elif line == "\n":
                if elves[elf_ix] > top_values[2]:
             
                    if elves[elf_ix] > top_values[1]:
                        
                        if elves[elf_ix] > top_values[0]:
                            top_values[2] = top_values[1]
                            top_values[1] = top_values[0]
                            top_values[0] = elves[elf_ix]

                            elf_ix += 1
                            elves.append(0)
                            
                            continue

                        top_values[2] = top_values[1]
                        top_values[1] = elves[elf_ix]
                        
                        elf_ix += 1
                        elves.append(0)
                        
                        continue

                    top_values[2] = elves[elf_ix]

                elf_ix += 1
                elves.append(0)

            else:
                elves[elf_ix] += int(line)



if __name__ == "__main__":
    path = "input_day1.txt"
    print(f"Total number of calories of top 3 elves is {load_input(path)}.")