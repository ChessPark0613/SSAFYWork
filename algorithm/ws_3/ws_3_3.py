T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    base = [list(map(int, input().split())) for _ in range(N)]
    chk = [[0] * (N - M + 1) for _ in range(N - M + 1)]

    max_value = 0

    for y in range(N - M + 1):
        for x in range(N - M + 1):
            kill_score = 0
            for dy in range(M):
                for dx in range(M):
                    kill_score += base[y + dy][x + dx]
            chk[y][x] = kill_score
            max_value = max(max_value, kill_score)

    print(f"#{test_case} {max_value}")
