
import re
from fractions import Fraction


BTN_RE = re.compile(r"\(([^)]*)\)")
REQ_RE = re.compile(r"\{([^}]*)\}")


def parse_line(line: str) -> tuple[list[list[int]], list[int]]:
    buttons = []
    for m in BTN_RE.finditer(line):
        raw = m.group(1).strip()
        if raw:
            buttons.append(list(map(int, raw.split(","))))
        else:
            buttons.append([])

    req = list(map(int, REQ_RE.search(line).group(1).split(",")))
    return buttons, req


def rref(A: list[list[int]], b: list[int]):
    r = len(A)
    m = len(A[0])

    M = [[Fraction(A[i][j]) for j in range(m)] + [Fraction(b[i])] for i in range(r)]

    pivots = []
    row = 0
    for col in range(m):
        pivot = None
        for i in range(row, r):
            if M[i][col] != 0:
                pivot = i
                break
        if pivot is None:
            continue

        M[row], M[pivot] = M[pivot], M[row]

        pv = M[row][col]
        for j in range(col, m + 1):
            M[row][j] /= pv

        for i in range(r):
            if i != row and M[i][col] != 0:
                f = M[i][col]
                for j in range(col, m + 1):
                    M[i][j] -= f * M[row][j]

        pivots.append(col)
        row += 1
        if row == r:
            break

    for i in range(r):
        if all(M[i][j] == 0 for j in range(m)) and M[i][m] != 0:
            return None, None, None

    free = [j for j in range(m) if j not in pivots]
    return M, pivots, free


def min_presses(A: list[list[int]], b: list[int]) -> int:
    M, pivots, free = rref(A, b)
    if M is None:
        raise ValueError("no solution")

    r = len(A)
    m = len(A[0])
    prow = {p: i for i, p in enumerate(pivots)}

    ubs = []
    for j in range(m):
        affected = [b[i] for i in range(r) if A[i][j] == 1]
        ubs.append(min(affected) if affected else 0)

    free_ubs = [ubs[j] for j in free]

    best = None

    def rec(idx: int, chosen: list[int]) -> None:
        nonlocal best
        if best is not None and sum(chosen) >= best:
            return

        if idx == len(free):
            x = [0] * m
            for j, v in zip(free, chosen):
                x[j] = v

            for p in pivots:
                i = prow[p]
                val = M[i][m]
                for j, v in zip(free, chosen):
                    c = M[i][j]
                    if c != 0:
                        val -= c * v
                if val.denominator != 1:
                    return
                iv = int(val)
                if iv < 0:
                    return
                x[p] = iv

            total = sum(x)
            if best is None or total < best:
                best = total
            return

        for v in range(free_ubs[idx] + 1):
            chosen.append(v)
            rec(idx + 1, chosen)
            chosen.pop()

    rec(0, [])

    if best is None:
        raise ValueError("no integer solution")
    return best


def solve(path: str) -> int:
    total = 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            buttons, req = parse_line(line)

            A = [[0] * len(buttons) for _ in range(len(req))]
            for j, idxs in enumerate(buttons):
                for i in idxs:
                    A[i][j] = 1

            total += min_presses(A, req)

    return total


if __name__ == "__main__":
    print(solve("input.txt"))
