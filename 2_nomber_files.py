a = []
b = []
with open('data.txt', 'r') as f:
    for line in f:
        line.strip()
        print(line)
        line.split()
        c = int('line')
        b.append(c)
        print(line)
        print(type(line))
        for i in b:
            if i % 2 == 0:
                a.append(i)
print(line)
print(a)