line_number = 1

with open("sample.txt", "r") as file:
    for line in file:
        print(str("line ") + str(line_number) + ". " + line.strip())
        line_number = line_number + 1