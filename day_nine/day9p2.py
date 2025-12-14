
from bisect import bisect_left
from itertools import combinations


def read_points(path: str) -> list[tuple[int, int]]:
    pts = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                x, y = map(int, line.split(","))
                pts.append((x, y))
    return pts


def point_in_poly(x: int, y: int, poly: list[tuple[int, int]]) -> bool:
    inside = False
    n = len(poly)

    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]

        if x1 == x2:
            if x == x1 and min(y1, y2) <= y <= max(y1, y2):
                return True

            y_low, y_high = (y1, y2) if y1 < y2 else (y2, y1)
            if y_low <= y < y_high and x1 > x:
                inside = not inside
        else:
            if y == y1 and min(x1, x2) <= x <= max(x1, x2):
                return True

    return inside


def build_axis(coords: list[int]) -> list[tuple[int, int]]:
    cols = []
    for i, a in enumerate(coords):
        cols.append((a, a))
        if i + 1 < len(coords):
            b = coords[i + 1]
            if b - a > 1:
                cols.append((a + 1, b - 1))
    return cols


def coord_to_idx(v: int, axis: list[tuple[int, int]], starts: list[int]) -> int:
    i = bisect_left(starts, v)
    if i == len(axis) or axis[i][0] != v:
        i -= 1
    a, b = axis[i]
    if not (a <= v <= b):
        raise ValueError("out of range")
    return i


def prefix_2d(mat: list[list[int]]) -> list[list[int]]:
    h = len(mat)
    w = len(mat[0])
    ps = [[0] * (w + 1) for _ in range(h + 1)]
    for y in range(h):
        row_sum = 0
        for x in range(w):
            row_sum += mat[y][x]
            ps[y + 1][x + 1] = ps[y][x + 1] + row_sum
    return ps


def rect_sum(ps: list[list[int]], y1: int, y2: int, x1: int, x2: int) -> int:
    y1 += 1
    y2 += 1
    x1 += 1
    x2 += 1
    return ps[y2][x2] - ps[y1 - 1][x2] - ps[y2][x1 - 1] + ps[y1 - 1][x1 - 1]


def solve(path: str) -> int:
    poly = read_points(path)
    xs = sorted(set(x for x, _ in poly))
    ys = sorted(set(y for _, y in poly))

    xaxis = build_axis(xs)
    yaxis = build_axis(ys)
    xstarts = [a for a, _ in xaxis]
    ystarts = [a for a, _ in yaxis]

    h = len(yaxis)
    w = len(xaxis)

    outside = [[0] * w for _ in range(h)]
    for yi, (ya, _) in enumerate(yaxis):
        for xi, (xa, _) in enumerate(xaxis):
            outside[yi][xi] = 0 if point_in_poly(xa, ya, poly) else 1

    ps = prefix_2d(outside)

    best = 0
    for (x1, y1), (x2, y2) in combinations(poly, 2):
        if x1 == x2 or y1 == y2:
            continue

        xa, xb = (x1, x2) if x1 < x2 else (x2, x1)
        ya, yb = (y1, y2) if y1 < y2 else (y2, y1)

        xi1 = coord_to_idx(xa, xaxis, xstarts)
        xi2 = coord_to_idx(xb, xaxis, xstarts)
        yi1 = coord_to_idx(ya, yaxis, ystarts)
        yi2 = coord_to_idx(yb, yaxis, ystarts)

        if rect_sum(ps, yi1, yi2, xi1, xi2) == 0:
            area = (xb - xa + 1) * (yb - ya + 1)
            if area > best:
                best = area

    return best


if __name__ == "__main__":
    print(solve("input.txt"))
