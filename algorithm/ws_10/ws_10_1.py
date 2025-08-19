T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    base = list(map(int, input().split()))


    def srp(i, j):
        a, b = base[i], base[j]
        if a == b:
            return i if i < j else j
        if (a, b) in [(1, 3), (2, 1), (3, 2)]:
            return i
        return j


    def game(l, r):
        if l == r:
            return l
        m = (l + r) // 2
        l_win = game(l, m)
        r_win = game(m + 1, r)
        return srp(l_win, r_win)


    winner = game(0, N - 1) + 1
    print(f"#{tc}",winner)