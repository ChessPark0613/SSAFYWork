from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    front = rear = 0

