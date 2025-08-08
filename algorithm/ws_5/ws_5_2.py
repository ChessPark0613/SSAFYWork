T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    base = [list(map(str, input())) for _ in range(N)]
    res = ''

    def _find(lst):
        for pos in range(N - M + 1):
            flag = True
            for i in range(M // 2):
                if lst[pos + i] != lst[pos + M - 1 - i]:
                    flag = False
                    break
            if flag:
                return lst[pos:pos + M]


    #가로
    for b in base:
        res = _find(b)
        if res:
            break

    #세로
    for x in range(N):
        if res:
            break

        tmp = ''
        for y in range(N):
            tmp += base[y][x]

        res = _find(tmp)
        if res:
            break

    print(f"#{test_case}", "".join(res))