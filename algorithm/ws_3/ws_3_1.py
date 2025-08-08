T = int(input())

def C(n):
    A = list(range(1, 13))
    res = []

    def chk(start, chosen):
        if len(chosen) == n:
            res.append(chosen[:])
            return

        for i in range(start, len(A)):
            chosen.append(A[i])
            chk(i+1, chosen)
            chosen.clear()

    chk(0, [])

    return res


for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    count_k = 0

    for case in C(N):
        if sum(case) == K:
            count_k += 1

    print(f"#{test_case} {count_k}")
