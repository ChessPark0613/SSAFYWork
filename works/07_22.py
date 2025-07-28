# ✅ 1. 튜플(Tuple) 생성 방법
tuple_1 = ()                      # 빈 튜플
tuple_2 = (1, 2, 3, 4)            # 일반적인 튜플
tuple_3 = (1,)                    # 단일 요소 튜플 (후행 쉼표 필수)
tuple_4 = 1, 2, 3, 4, 5           # 괄호 생략 가능 (암묵적 튜플 패킹)
tuple_5 = tuple([10, 20, 30])     # iterable 객체 → 튜플로 변환

# ✅ 2. 단일 요소 튜플 vs 일반 괄호
print(type((1)))   # <class 'int'>
print(type((1,)))  # <class 'tuple'>

# ✅ 3. 불변성(Immutability)
# 튜플은 요소의 추가/삭제/변경이 불가능
immutable_example = (1, 2, 3)
# immutable_example[0] = 10  # TypeError 발생

# ✅ 4. 이건뭐지
# 불변성을 가지는 튜플 내부에 리스트가 있으면 리스트는 변경 가능하다..?!
num_a = 5
num_b = 6
tuple_test = ([1,2,3], num_a, num_b)
tuple_test[0][1] = 5
print(tuple_test)
# String 도 가능한가? - 문자열은 불변이여서 안됨
# tuple_test_2 = ('hellow', 1, 2, 3)
# tuple_test_2[0][0] = 'H'
# print(tuple_test_2)

# ✅ 5. 딕셔너리
# 걍 key & value