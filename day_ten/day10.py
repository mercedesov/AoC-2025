
import re


DIAG_RE = re.compile(r"\[([.#]+)\]")
BTN_RE = re.compile(r"\(([^)]*)\)")


def parse_line(line: str) -> tuple[int, list[int]]:
    diag = DIAG_RE.search(line).group(1)

    target = 0
    for i, ch in enumerate(diag):
        if ch == "#":
            target |= 1 << i

    masks = []
    for m in BTN_RE.finditer(line):
        raw = m.group(1).strip()
        if not raw:
            masks.append(0)
            continue
        idxs = map(int, raw.split(","))
        mask = 0
        for k in idxs:
            mask |= 1 << k
        masks.append(mask)

    return target, masks


def min_presses(target: int, masks: list[int]) -> int:
    m = len(masks)
    xors = [0] * (1 << m)

    for s in range(1, 1 << m):
        lsb = s & -s
        j = (lsb.bit_length() - 1)
        xors[s] = xors[s ^ lsb] ^ masks[j]

    best = 10**9
    for s, v in enumerate(xors):
        if v == target:
            pc = s.bit_count()
            if pc < best:
                best = pc
                if best == 0:
                    break

    return best


def solve(path: str) -> int:
    total = 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            target, masks = parse_line(line)
            total += min_presses(target, masks)
    return total


if __name__ == "__main__":
    print(solve("input.txt"))
