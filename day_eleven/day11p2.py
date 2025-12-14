
from collections import defaultdict

SPECIAL = {"dac": 1, "fft": 2}


def read_graph(path: str) -> dict[str, list[str]]:
    g: dict[str, list[str]] = defaultdict(list)
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            src, dsts = line.split(":", 1)
            g[src.strip()] = dsts.strip().split()
    return g


def solve(path: str) -> int:
    g = read_graph(path)
    memo: dict[tuple[str, int], int] = {}
    visiting: set[tuple[str, int]] = set()

    def dfs(u: str, mask: int) -> int:
        mask |= SPECIAL.get(u, 0)

        if u == "out":
            return 1 if mask == 3 else 0

        key = (u, mask)
        if key in memo:
            return memo[key]
        if key in visiting:
            raise ValueError("cycle detected")

        visiting.add(key)
        total = 0
        for v in g.get(u, []):
            total += dfs(v, mask)
        visiting.remove(key)

        memo[key] = total
        return total

    return dfs("svr", 0)


if __name__ == "__main__":
    print(solve("input.txt"))
