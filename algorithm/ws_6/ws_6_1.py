T = int(input())

for test_case in range(1, T + 1):
    str1 = list(input())
    str2 = list(input())

    res = 0
    dic1 = dict()
    dic2 = dict()

    for b in str2:
        dic2[b] = dic2.get(b, 0) + 1

    for a in str1:
        if res < dic2.get(a):
            res = dic2.get(a)


    print(f"#{test_case} {res}")