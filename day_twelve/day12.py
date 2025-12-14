
SHAPE_CELLS = [7, 7, 7, 6, 7, 5]

def solve(path: str) -> int:
    ok = 0
    with open(path, encoding="utf-8") as f:
        lines = [ln.strip() for ln in f if ln.strip()]

    i = 0
    while i < len(lines) and lines[i].endswith(":"):
        i += 1
        while i < len(lines) and set(lines[i]) <= {".", "#"}:
            i += 1

    for ln in lines[i:]:
        dims, counts = ln.split(":", 1)
        w, h = map(int, dims.split("x"))
        q = list(map(int, counts.split()))
        need = sum(a * b for a, b in zip(q, SHAPE_CELLS))
        if need <= w * h:
            ok += 1

    return ok


if __name__ == "__main__":
    print(solve("input.txt"))
