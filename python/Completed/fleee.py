with open('scratch.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    print(line, end = '')

with open('scratch.txt', w) as file:
    new_lines = ('I took your milkshake!\n\n I drank it down?')

for line in new_lines:
    file.write(line)

with open('scratch.txt', 'a') as a_file:
    new_lines = lines

    for line in new_lines:
        a_file.write(lines)