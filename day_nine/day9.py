
import itertools


def solve(path: str) -> int:
    points = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                x, y = map(int, line.split(","))
                points.append((x, y))

    max_area = 0
    for (x1, y1), (x2, y2) in itertools.combinations(points, 2):
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        if area > max_area:
            max_area = area

    return max_area


if __name__ == "__main__":
    print(solve("input.txt"))
