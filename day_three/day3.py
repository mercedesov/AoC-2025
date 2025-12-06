def max_joltage(line: str) -> int:
    s = line.strip()
    best = -1
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            v = int(s[i]) * 10 + int(s[j])
            if v > best:
                best = v
    return best


total = 0

with open("input.txt") as f:  
    for line in f:
        line = line.strip()
        if not line:
            continue
        total += max_joltage(line)

print(total)
