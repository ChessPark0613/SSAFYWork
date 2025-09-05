def solve_case(cost):
    N = len(cost)
    INF = float("inf")
    tmp = {}

    def dfs(u, chk):
        if all(chk):
            return cost[u][0]

        key = (u, tuple(chk))
        if key in tmp:
            return tmp[key]

        best = INF
        for v in range(N):
            if not chk[v]:
                chk[v] = True
                cand = cost[u][v] + dfs(v, chk)
                best = min(best, cand)
                chk[v] = False
        tmp[key] = best
        return best

    chk = [False] * N
    chk[0] = True
    return dfs(0, chk)

if __name__ == "__main__":
    T = int(input().strip())
    for tc in range(1, T + 1):
        N = int(input().strip())
        cost = [list(map(int, input().split())) for _ in range(N)]
        ans = solve_case(cost)
        print(f"#{tc} {ans}")
