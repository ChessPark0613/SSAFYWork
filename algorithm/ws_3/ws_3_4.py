T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    base = [list(map(int, input().split())) for _ in range(N)]
    count = 0

    for y in range(N):
        x = 0
        while x <= N - K:
            if all(base[y][x + i] == 1 for i in range(K)):
                left_ok = (x == 0) or (base[y][x - 1] == 0)
                right_ok = (x + K == N) or (base[y][x + K] == 0)

                if left_ok and right_ok:
                    count += 1
                x += K
            else:
                x += 1

    for x in range(N):
        y = 0
        while y <= N - K:
            if all(base[y + i][x] == 1 for i in range(K)):
                up_ok = (y == 0) or (base[y - 1][x] == 0)
                down_ok = (y + K == N) or (base[y + K][x] == 0)

                if up_ok and down_ok:
                    count += 1
                y += K
            else:
                y += 1
    print(f"#{test_case} {count}")

"""
1
5 3
1 0 0 1 0
1 1 0 1 1
1 0 1 1 1
0 1 1 0 1
0 1 1 1 0
"""
