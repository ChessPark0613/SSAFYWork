T = int(input())

for test_case in range(1, T + 1):
    base = list(map(str, input()))

    length = len(base)
    target = 0

    while target < length - 1:
        if base[target] == base[target + 1]:
            base[target:] = base[target + 2:]
            target = max(0, target - 1)
            length -= 2
            continue

        target += 1



    print(f"#{test_case}", len(base))