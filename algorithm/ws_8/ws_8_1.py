T = int(input().strip())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    base = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        base[a].append(b)

    S, G = map(int, input().split())
    visited = [False] * (V + 1)
    stack = [S]
    visited[S] = True
    res = 0

    while stack:
        node = stack.pop()
        if node == G:
            res = 1
            break
        for v in base[node]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)

    print(f"#{tc}", res)
