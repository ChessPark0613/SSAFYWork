T = int(input())
for tc in range(1, T + 1):
    token = list(input().split())
    stack = []

    for sign in token:
        try:
            sign = int(sign)
            stack.append(sign)
        except:
            if sign != '.':
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    if sign == '+':
                        result = b + a
                    elif sign == '-':
                        result = b - a
                    elif sign == '*':
                        result = b * a
                    elif sign == '/':
                        result = b / a

                    stack.append(int(result))
                else:
                    print(f'#{tc} error')
                    break
            else:
                if len(stack) == 1:
                    print(f'#{tc} {stack.pop()}')
                    break
                else:
                    print(f'#{tc} error')
                    break

