
raw = open("input.txt").read().strip().splitlines()

i = raw.index("")
range_lines = raw[:i]
id_lines = raw[i+1:]

ranges = []
for line in range_lines:
    a, b = map(int, line.split("-"))
    ranges.append((a, b))

ranges.sort()
merged = []
for a, b in ranges:
    if not merged or a > merged[-1][1] + 1:
        merged.append([a, b])
    else:
        merged[-1][1] = max(merged[-1][1], b)

fresh = 0
for line in id_lines:
    x = int(line)
    # binary search in merged intervals
    lo, hi = 0, len(merged) - 1
    ok = False
    while lo <= hi:
        mid = (lo + hi) // 2
        a, b = merged[mid]
        if a <= x <= b:
            ok = True
            break
        if x < a:
            hi = mid - 1
        else:
            lo = mid + 1
    if ok:
        fresh += 1

print(fresh)
