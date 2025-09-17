T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]

    used = [False] * N
    ans = float("inf")


    def dfs(i, total):
        global ans
        if total >= ans:
            return
        if i == N:
            ans = min(ans, total)
            return
        for j in range(N):
            if not used[j]:
                used[j] = True
                dfs(i + 1, total + cost[i][j])
                used[j] = False


    dfs(0, 0)
    print(f"#{tc} {ans}")
