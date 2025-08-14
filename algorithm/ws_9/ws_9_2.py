T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    base = [list(map(int, input().strip())) for _ in range(N)]
    chk = [[False] * N for _ in range(N)]
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    flag = False
    queue = []

    for y in range(N):
        for x in range(N):
            target = base[y][x]
            if target == 2:
                queue.append((y, x))
            if target == 1:
                chk[y][x] = True

    while queue:
        y, x = queue.pop()
        if base[y][x] == 3:
            flag = True
            break

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < N and 0 <= nx < N:
                if not chk[ny][nx]:
                    chk[ny][nx] = True
                    queue.append((ny, nx))

    if flag:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")