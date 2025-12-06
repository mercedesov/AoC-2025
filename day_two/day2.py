with open("input.txt") as f:
    ranges = f.read().strip()

def is_invalid(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    m = len(s) // 2
    return s[:m] == s[m:]

total = 0

for r in ranges.split(','):
    a, b = map(int, r.split('-'))
    for x in range(a, b + 1):
        if is_invalid(x):
            total += x

print(total)
