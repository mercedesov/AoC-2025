
data = [line.rstrip() for line in open("input.txt") if line.strip()]

h = len(data)
w = len(data[0])
cnt = 0

for r in range(h):
    for c in range(w):
        if data[r][c] != '@':
            continue
        adj = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr = r + dr
                nc = c + dc
                if 0 <= nr < h and 0 <= nc < w:
                    if data[nr][nc] == '@':
                        adj += 1
        if adj < 4:
            cnt += 1

print(cnt)
