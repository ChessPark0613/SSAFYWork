T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    base = sorted(list(map(int, input().split())))
    res = []
    left = 0
    right = N - 1

    while len(res) < 10:
        if len(res) < 10:
            res.append(base[right])
            right -= 1
        if len(res) < 10:
            res.append(base[left])
            left += 1

    print(f"#{test_case}", *res)