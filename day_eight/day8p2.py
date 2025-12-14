
import numpy as np


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, a: int) -> int:
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

    def union(self, a: int, b: int) -> bool:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True


def read_points(path: str) -> np.ndarray:
    pts = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            pts.append(tuple(map(int, line.split(","))))
    return np.array(pts, dtype=np.int64)


def solve(path: str) -> int:
    pts = read_points(path)
    n = len(pts)

    edges = []
    for i in range(n - 1):
        dif = pts[i + 1:] - pts[i]
        d2 = (dif * dif).sum(axis=1)
        js = np.arange(i + 1, n, dtype=np.int32)
        edges.extend(zip(d2.tolist(), [i] * len(js), js.tolist()))

    edges.sort(key=lambda t: t[0])

    dsu = DSU(n)
    last_i = last_j = 0

    for _, i, j in edges:
        if dsu.union(i, j):
            last_i, last_j = i, j
            if dsu.components == 1:
                break

    return int(pts[last_i, 0] * pts[last_j, 0])


if __name__ == "__main__":
    print(solve("input.txt"))
