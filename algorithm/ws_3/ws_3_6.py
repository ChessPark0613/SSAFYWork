for _ in range(1, 11):
    test_case = int(input())
    base = [list(map(int, input().split())) for _ in range(100)]
    right_dgi = 0
    left_dgi = 0
    max_row = 0
    max_col = 0
    row_sum = [0] * 100
    col_sum = [0] * 100

    for y in range(100):
        for x in range(100):
            if x == y:
                right_dgi += base[y][x]
                left_dgi += base[99 - y][99 - x]

            row_sum[y] += base[y][x]
            col_sum[x] += base[y][x]

    for r in row_sum:
        if max_row < r:
            max_row = r

    for c in col_sum:
        if max_col < c:
            max_col = c

    t = (max_row, max_col, right_dgi, left_dgi)
    res = 0
    for a in t:
        if res < a:
            res = a

    print(f"#{test_case} {res}")

