T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    res = []

    for y in range(N):
        row = [1] * (y + 1)
        for x in range(1, y):
            row[x] = res[y - 1][x - 1] + res[y - 1][x]
        res.append(row)

    print(f"#{test_case}")
    for row in res:
        print(*row)
