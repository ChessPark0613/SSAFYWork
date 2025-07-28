# 아래 함수를 수정하시오.
def even_elements(lst):
    for item in lst:
        if int(item) % 2:
            lst.pop(lst.index(item))

    return lst


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
restult = even_elements(my_list)
print(restult)
