import random

lines = []
buf = ""

files = ['main.c', 'main.py']


with open(random.choice(files), 'r') as file:
    lines = file.read().split('\n')
    llen = len(lines)


while random.random() < 0.97:
    buf += f"{random.choice(lines)}\n"

with open("gen.py", 'w') as file:
    file.write(buf)
