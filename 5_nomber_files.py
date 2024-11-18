a = []
with open('part1.txt', 'r') as f:
    for line in f:
        a.append(line)
b = []
with open('part2.txt', 'r') as f1:
    for line in f1:
        a.append(line)

with open('full_text.txt', 'a') as f3:
    f3.write(a)
    f3.write(b)