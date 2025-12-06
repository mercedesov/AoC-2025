
def solve():
    with open("input.txt") as f:
        text = f.read().strip()

    # split into: [ranges-block, ids-block]
    parts = text.split("\n\n")
    ranges_block = parts[0].splitlines()

    ranges = []
    for line in ranges_block:
        a, b = line.split("-")
        ranges.append((int(a), int(b)))

    ranges.sort()
    merged = []

    for a, b in ranges:
        if not merged or a > merged[-1][1] + 1:
            merged.append([a, b])
        else:
            merged[-1][1] = max(merged[-1][1], b)

    total = sum(b - a + 1 for a, b in merged)
    print(total)


if __name__ == "__main__":
    solve()
