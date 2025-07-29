# 아래 함수를 수정하시오.
def remove_duplicates_to_set(lst):
    result = set()
    for num in lst:
        if num not in result:
            result.add(num)
    return result


result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)
