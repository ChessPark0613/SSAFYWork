T = 10

for test_case in range(1, T + 1):
    N = int(input())
    base_len = 8
    base = [list(map(str, input())) for _ in range(base_len)]
    res = 0

    def _find(lst):
        s = 0
        for pos in range(base_len - N + 1):
            flag = True
            for i in range(N // 2):
                if lst[pos + i] != lst[pos + N - 1 - i]:
                    flag = False
                    break
            if flag:
                s += 1

        return s


    for b in base:
        res += _find(b)

    for x in range(base_len):
        tmp = []
        for y in range(base_len):
            tmp.extend(base[y][x])

        res += _find(tmp)

    print(f"#{test_case}", res)