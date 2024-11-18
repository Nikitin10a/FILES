from idlelib.replace import replace
a = []
with open('message.txt', 'r') as f:
    for i in f:
        a.append(replace(i, (i+3)))

with open('encrypted_message.txt', 'w') as f1:
    f1.write(a)
        
