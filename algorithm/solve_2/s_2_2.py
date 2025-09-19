### 보급로
import sys

sys.stdin = open("s_2_2_in.txt", "r")

T = int(input().strip())

for tc in range(1, T + 1):
    N = int(input().strip())
    arr = [list(map(int, input())) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]

    for k in range(1, N):
        dp[0][k] = dp[0][k - 1] + arr[0][k]
        dp[k][0] = dp[k - 1][0] + arr[k][0]

    for y in range(1, N):
        for x in range(1, N):
            dp[y][x] = min(arr[y][x] + dp[y - 1][x], arr[y][x] + dp[y][x - 1])

    print(f"#{tc} {dp[N - 1][N - 1]}")
