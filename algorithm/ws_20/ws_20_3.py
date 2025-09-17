T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    print(visited)
    t = {
        "1":(0, 1, 2, 3),
        "2":(0, 2),
        "3":(1, 3),
        "4":(0, 1),
        "5":(1, 2),
        "6":(2, 3),
        "7":(0, 3),
    }

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

