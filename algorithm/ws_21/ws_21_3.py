def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    direction = 0  # 0 = 시작, 1 = 왼쪽, 2 = 오른쪽
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            return True
        elif arr[m] < target:
            if direction == 2:  # 연속 같은 방향이면 탈락
                return False
            direction = 2
            l = m + 1
        else:
            if direction == 1:
                return False
            direction = 1
            r = m - 1
    return False


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    ans = 0
    for b in B:
        if binary_search(A, b):
            ans += 1
    print(f"#{tc} {ans}")