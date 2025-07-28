# 아래 함수를 수정하시오.
def count_character(str, char):
    count = sum(map(lambda x: x == char,str))
    return count


result = count_character("Hello, World!", "o")
print(result)  # 2
