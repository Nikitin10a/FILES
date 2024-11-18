with open('text.txt.txt', 'r') as f:
    s = 0
    sw = 0
    b = 0
    for line in f:
        s += 1
        sw += len(line.split())
        b = len(line)
print("Строки: ", s, "Слова: ", sw, "Буквы:", b)















