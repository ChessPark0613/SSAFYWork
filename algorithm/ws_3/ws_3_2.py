T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    case = [list(map(int, input().split())) for _ in range(N)]
    base = [[0] * 10 for _ in range(10)]
    count = 0

    for box in case:
        r1, c1, r2, c2, color = box

        for y in range(c1, c2 + 1):
            for x in range(r1, r2 + 1):
                base_color = base[y][x]
                if color != base_color:
                    base[y][x] = base_color + color
                    if base[y][x] == 3:
                        count += 1

    print(f"#{test_case} {count}")
