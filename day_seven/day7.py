with open("input.txt", encoding="utf-8") as f:
    grid = f.read().splitlines()

width = len(grid[0])
height = len(grid)

start_x = grid[0].index("S")

beams = {start_x}
splits = 0

for y in range(1, height):
    next_beams = set()

    for x in beams:
        if grid[y][x] == "^":
            splits += 1
            if x > 0:
                next_beams.add(x - 1)
            if x < width - 1:
                next_beams.add(x + 1)
        else:
            next_beams.add(x)

    beams = next_beams

print(splits)
