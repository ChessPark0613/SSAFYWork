T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    res = 0


    def mul(arr, target):
        l, r = 0, len(arr) - 1
        prev = 0

        while l <= r:
            m = (l + r) // 2
            if arr[m] == target:  # 통과
                return True

            if arr[m] > target: # 왼쪽 구간
                if prev != 1:
                    prev = 1
                    r = m - 1
                else:
                    return False
            elif arr[m] < target: # 오른쪽 구간
                if prev != 2:
                    prev = 2
                    l = m + 1
                else:
                    return False


    for b in B:
        if mul(A, b): res += 1

    print(f"#{test_case} {res}")
