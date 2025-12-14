
from collections import defaultdict


def count_timelines(grid: list[str]) -> int:
    width = len(grid[0])
    height = len(grid)

    start_x = grid[0].index("S")

    timelines: dict[int, int] = {start_x: 1}

    for y in range(1, height):
        next_timelines = defaultdict(int)

        for x, count in timelines.items():
            if grid[y][x] == "^":
                if x > 0:
                    next_timelines[x - 1] += count
                if x < width - 1:
                    next_timelines[x + 1] += count
            else:
                next_timelines[x] += count

        timelines = next_timelines

    return sum(timelines.values())


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        manifold = f.read().splitlines()

    print(count_timelines(manifold))
