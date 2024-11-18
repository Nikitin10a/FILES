from idlelib.replace import replace

s = 0
with open('story1.txt', 'r') as f:
    for line in f:
        s = len(line.split())
        if s == 'Python':
            replace('Python', 'Java')
with open('new_story.txt', 'w') as f1:
    f1.write(f1)