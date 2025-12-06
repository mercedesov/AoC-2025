
pos = 50
count = 0

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        d = line[0]
        n = int(line[1:])

        if d == "L":
            pos = (pos - n) % 100
        else: 
            pos = (pos + n) % 100

        if pos == 0:
            count += 1

print(count) 
