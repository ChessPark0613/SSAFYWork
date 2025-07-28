# 아래 함수를 수정하시오.
def sort_tuple(tpl):
    list_tpl = sorted(list(tpl))
    new_tuple = tuple(list_tpl)
    
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
