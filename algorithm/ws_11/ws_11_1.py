from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cheeses = list(map(int, input().split()))

    oven = deque((i + 1, cheeses[i]) for i in range(N))
    next_chees = N

    while len(oven) > 1:
        num, chees = oven.popleft()
        chees //= 2
        if chees == 0:
            if next_chees < M:
                oven.append((next_chees + 1, cheeses[next_chees]))
                next_chees += 1
        else:
            oven.append((num, chees))

    last_num, _ = oven[0]
    print(f"#{tc} {last_num}")
