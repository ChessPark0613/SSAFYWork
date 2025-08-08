T = int(input())

for test_case in range(1, T + 1):
    base = [list(map(int, input().split())) for _ in range(9)]
    row = True
    col = True
    box = True

    for tmp in base:
        col_chk = [False] * 9
        for i in tmp:
            col_chk[i - 1] = True

        if not all(c == True for c in col_chk):
            row = False
            break


    for x in range(9):
        row_chk = [False] * 9
        for y in range(9):
            num = int(base[y][x])
            row_chk[num - 1] = True

        if not all(r == True for r in row_chk):
            col = False
            break

# 00, 03, 06
# 30, 33, 36
# 60, 63, 66
    for sy in range(0, 9, 3):
        for sx in range(0, 9, 3):
            box_chk = [False] * 9
            for dy in range(3):
                for dx in range(3):
                    num = base[sy + dy][sx + dx]
                    box_chk[num - 1] = True

            if not all(box_chk):
                box = False
                break
        if not box:
            break

    if row and col:
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")
