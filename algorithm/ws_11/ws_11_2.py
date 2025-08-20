from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    nums = deque(map(int, input().split()))
    res = 0

    for x in range(M):
        nums.append(nums.popleft())
        if x == M - 1:
            res = nums.popleft()

    print(f"#{tc} {res}")