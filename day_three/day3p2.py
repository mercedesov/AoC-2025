
def best12(s: str) -> int:
    k = 12     
    out = []
    start = 0
    n = len(s)

    while k > 0:
        # choose best digit in window [start .. n-k]
        end = n - k + 1
        best = '0'
        best_i = start

        for i in range(start, end):
            d = s[i]
            if d > best:
                best = d
                best_i = i
                if d == '9': 
                    break

        out.append(best)
        start = best_i + 1
        k -= 1

    return int("".join(out))


def solve():
    total = 0
    with open("input.txt") as f:
        for line in f:
            s = line.strip()
            if s.isdigit():
                total += best12(s)
    print(total)


if __name__ == "__main__":
    solve()
