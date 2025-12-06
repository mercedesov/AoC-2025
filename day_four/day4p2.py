
def neighbors_count(g, r, c, R, C):
    cnt = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr = r + dr
            nc = c + dc
            if 0 <= nr < R and 0 <= nc < C and g[nr][nc] == '@':
                cnt += 1
    return cnt


def solve():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    lines = [ln for ln in lines if ln.strip()]

    grid = [list(ln) for ln in lines]
    R = len(grid)
    C = len(grid[0])

    total = 0

    while True:
        removable = []
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '@':
                    if neighbors_count(grid, r, c, R, C) < 4:
                        removable.append((r, c))

        if not removable:
            break

        for r, c in removable:
            grid[r][c] = '.'

        total += len(removable)

    print(total)


if __name__ == "__main__":
    solve()
