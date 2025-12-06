
with open("input.txt") as f:
    ops = [line.strip() for line in f]

pos = 50
count = 0

for op in ops:
    d = op[0]
    n = int(op[1:])

    for _ in range(n):
        pos = (pos - 1) % 100 if d == "L" else (pos + 1) % 100
        if pos == 0:
            count += 1

print(count)
