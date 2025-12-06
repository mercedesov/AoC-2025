
def repeated(s: str) -> bool:
    L = len(s)
    for d in range(1, L):
        if L % d == 0:
            if s == s[:d] * (L // d):
                return True
    return False


def parse_ranges(line):
    for part in line.split(","):
        if part:
            a, b = part.split("-")
            yield int(a), int(b)


def solve():
    with open("input.txt") as f:
        line = f.read().strip()

    total = 0
    for lo, hi in parse_ranges(line):
        for x in range(lo, hi + 1):
            if repeated(str(x)):
                total += x

    print(total)


if __name__ == "__main__":
    solve()
