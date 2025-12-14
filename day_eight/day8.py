
import heapq
from collections import defaultdict


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, a: int) -> int:
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

    def union(self, a: int, b: int) -> None:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]


def read_points(path: str) -> list[tuple[int, int, int]]:
    points: list[tuple[int, int, int]] = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x, y, z = map(int, line.split(","))
            points.append((x, y, z))
    return points


def k_smallest_edges(points: list[tuple[int, int, int]], k: int) -> list[tuple[int, int, int]]:
    n = len(points)
    heap: list[tuple[int, int, int]] = []

    for i in range(n):
        xi, yi, zi = points[i]
        for j in range(i + 1, n):
            xj, yj, zj = points[j]
            dx = xi - xj
            dy = yi - yj
            dz = zi - zj
            d2 = dx * dx + dy * dy + dz * dz

            if len(heap) < k:
                heapq.heappush(heap, (-d2, i, j))
            else:
                if -d2 > heap[0][0]:
                    heapq.heapreplace(heap, (-d2, i, j))

    edges = [(-neg_d2, i, j) for neg_d2, i, j in heap]
    edges.sort()
    return edges


def solve(path: str) -> int:
    points = read_points(path)
    edges = k_smallest_edges(points, 1000)

    dsu = DSU(len(points))
    for _, a, b in edges:
        dsu.union(a, b)

    comp = defaultdict(int)
    for i in range(len(points)):
        comp[dsu.find(i)] += 1

    sizes = sorted(comp.values(), reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


if __name__ == "__main__":
    print(solve("input.txt"))
