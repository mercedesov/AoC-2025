
from math import prod

with open("input.txt") as f:
    lines = [ln.rstrip("\n") for ln in f if ln.strip()]

grid = lines
rows = len(grid)
cols = len(grid[0])

active = [
    any(grid[r][c] != " " for r in range(rows))
    for c in range(cols)
]

ranges = []
c = 0
while c < cols:
    if not active[c]:
        c += 1
        continue
    start = c
    while c < cols and active[c]:
        c += 1
    end = c - 1
    ranges.append((start, end))

def parse_problem(col_start, col_end):
    nums = []
    # rows 0..rows-2: numbers
    for r in range(rows - 1):
        seg = grid[r][col_start:col_end + 1]
        digits = "".join(ch for ch in seg if ch.isdigit())
        if digits:
            nums.append(int(digits))

    # last row: operator
    op_seg = grid[rows - 1][col_start:col_end + 1]
    op = next(ch for ch in op_seg if ch in "+*")
    return nums, op

total = 0
for a, b in ranges:
    nums, op = parse_problem(a, b)
    if op == "+":
        total += sum(nums)
    else:
        total += prod(nums)

print(total)
