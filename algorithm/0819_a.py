T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    can_fail = N - M
    r = M // K
    chk = [True] * (N + 1)
    chk[0] = False
    res = 0

    for x in range(N, 0, -1):
        if can_fail > 0:
            if x % K == 0:
                chk[x] = False
                can_fail -= 1

    if can_fail > 0:
        for i in range(N, N - can_fail, -1):
            chk[i] = False

    for i in range(1, N + 1):
        if chk[i]:
            if i % K == 0:
                res += 1
                res *= 2
            else:
                res += 1

    print(f"#{tc}", res)

