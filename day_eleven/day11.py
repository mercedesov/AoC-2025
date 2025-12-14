
from collections import defaultdict


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


def count_paths(g: dict[str, list[str]], start: str, target: str) -> int:
    visiting = set()
    memo: dict[str, int] = {}

    def dfs(u: str) -> int:
        if u == target:
            return 1
        if u in memo:
            return memo[u]
        if u in visiting:
            raise ValueError("cycle detected")
        visiting.add(u)

        total = 0
        for v in g.get(u, []):
            total += dfs(v)

        visiting.remove(u)
        memo[u] = total
        return total

    return dfs(start)


if __name__ == "__main__":
    graph = read_graph("input.txt")
    print(count_paths(graph, "you", "out"))
