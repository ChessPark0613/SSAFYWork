# 아래 함수를 수정하시오.
def union_sets(set_1, set_2):
    return set_1.union(set_2)

def union_multiple_sets(*sets):
    if len(sets) < 2:
        print("최소 두 개의 셋이 필요합니다.")
        return 

    return set().union(*sets)




result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)  # {1, 2, 3, 4, 5}

result = union_multiple_sets({1, 2}, {3, 4}, {5, 6})
print(result)  # {1, 2, 3, 4, 5, 6}

result = union_multiple_sets({1, 2})
# 출력 : 최소 두 개의 셋이 필요합니다
