def check_number():
    print('숫자를 입력하세요 : ', end='')
    input_num = input()
    try:
        num = int(input_num)
        if num > 0:
            print('양수입니다.')
        elif num < 0:
            print('음수입니다.')
        else:
            print('0입니다.')
    except ValueError:
        print('잘못된 입력입니다.')



check_number()
