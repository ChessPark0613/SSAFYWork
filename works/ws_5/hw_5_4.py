# 아래 함수를 수정하시오.
def find_min_max(lst):
    min_num, max_num = lst[0], lst[0]
    for num in lst:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    return (min_num, max_num)


result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
