T = int(input())

for tc in range(1, T + 1):
    N = int(input()) // 10
    res = 0


    def factorial(n):
        r = 1
        for i in range(2, n + 1):
            r *= i
        return r


    def dp():
        global N, res
        for x in range(0, N // 2 + 1):
            case = factorial(N - x) // (factorial(x) * factorial(N - (2 * x)))
            res += case * (2 ** x)

        print(f"#{tc} {res}")

    dp()
