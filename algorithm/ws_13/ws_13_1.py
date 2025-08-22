T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())

    tree = []
    while len(tree) < 2 * E:
        tree += list(map(int, input().split()))


    children = [[] for _ in range(E + 2)]
    for i in range(0, 2 * E, 2):
        p, c = tree[i], tree[i + 1]
        children[p].append(c)

    cnt = 0
    stack = [N]
    while stack:
        v = stack.pop()
        cnt += 1
        for ch in children[v]:
            stack.append(ch)

    print(f"#{tc} {cnt}")