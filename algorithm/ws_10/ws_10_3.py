T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    base = [list(map(int, input().split())) for _ in range(N)]

    def comb():
        global N, base
        chk = [False] * N
        res = float("inf")

        def dfs(y, sum):
            nonlocal res
            if sum > res:
                return

            if y == N:
                res = min(res, sum)
                return

            for x in range(N):
                if not chk[x]:
                    chk[x] = True
                    dfs(y + 1, sum + base[y][x])
                    chk[x] = False

        dfs(0, 0)
        return res

    print(f"#{tc}", comb())