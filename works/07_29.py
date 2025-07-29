"""
딕셔너리 조회 방식 비교: my_dict['key'] vs my_dict.get('key')
"""

# 샘플 딕셔너리
my_dict = {'name': 'John', 'age': 30}

# 1. my_dict['key']
# - 키가 반드시 존재해야 함
# - 존재하지 않으면 KeyError 발생

print(my_dict['name'])  # 'John'
# print(my_dict['email'])  # ❌ KeyError 발생 (주석 처리됨)

# 2. my_dict.get('key')
# - 키가 없어도 예외가 발생하지 않음
# - 기본값 지정 가능

print(my_dict.get('name'))       # 'John'
print(my_dict.get('email'))      # None
print(my_dict.get('email', 'N/A'))  # 'N/A'

# 요약 비교
"""
| 구분                     | my_dict['key']         | my_dict.get('key')               |
|--------------------------|-------------------------|-----------------------------------|
| 키 존재 여부             | 반드시 존재해야 함       | 없어도 됨                          |
| 존재하지 않을 경우       | KeyError 예외 발생       | None 또는 기본값 반환              |
| 기본값 지정 가능 여부    | ❌                        | ✅ my_dict.get('key', default)     |
| 일반적인 사용 상황       | 키 존재가 확실할 때 사용  | 키가 없을 수도 있을 때 사용        |
"""

# 실전 팁:
# 외부 데이터나 사용자 입력 등 불확실한 키를 다룰 때는 get() 사용을 권장!

"""
파이썬 딕셔너리 메서드 정리
"""

my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'Seoul'
}

# 1. keys() : 딕셔너리의 모든 키 반환
print(my_dict.keys())  # dict_keys(['name', 'age', 'city'])

# 2. values() : 딕셔너리의 모든 값 반환
print(my_dict.values())  # dict_values(['Alice', 25, 'Seoul'])

# 3. items() : (키, 값) 쌍 반환
print(my_dict.items())  # dict_items([('name', 'Alice'), ('age', 25), ('city', 'Seoul')])

# 4. get(key, default=None) : 키로 값 조회 (없으면 None 또는 기본값 반환)
print(my_dict.get('age'))        # 25
print(my_dict.get('gender'))     # None
print(my_dict.get('gender', 'N/A'))  # 'N/A'

# 5. update(dict2) : 기존 딕셔너리에 다른 딕셔너리를 병합 (덮어씀)
my_dict.update({'age': 30, 'country': 'Korea'})
print(my_dict)  # {'name': 'Alice', 'age': 30, 'city': 'Seoul', 'country': 'Korea'}

# 6. pop(key, default=None) : 키로 항목 제거 후 값 반환 (없으면 기본값 또는 에러)
print(my_dict.pop('city'))       # 'Seoul'
# print(my_dict.pop('city'))     # ❌ KeyError
print(my_dict.pop('job', '없음'))  # '없음'

# 7. popitem() : 마지막 (key, value) 쌍 제거 (Python 3.7+)
print(my_dict.popitem())  # ('country', 'Korea') 등

# 8. clear() : 딕셔너리 비우기
my_dict.clear()
print(my_dict)  # {}

# 9. setdefault(key, default=None) : 키가 없으면 기본값으로 삽입하고 값을 반환
# update() : 키 존재 여부 상관없이 값을 추가하거나 덮어씀
# setdefault() : 키가 없을 때만 값을 추가, 키가 이미 있으면 기존 값 유지

d = {'a': 1}
print(d.setdefault('a', 100))  # 1 (이미 있음)
print(d.setdefault('b', 200))  # 200 (새로 추가됨)
print(d)  # {'a': 1, 'b': 200}

# 10. copy() : 얕은 복사본 반환
original = {'x': 10, 'y': 20}
copy_dict = original.copy()
print(copy_dict)  # {'x': 10, 'y': 20}
print(copy_dict is original)  # False


'''
set : 고유한 항목들의 정렬되지 않은 컬렉션

- 해시 테이블을 사용하여 데이터 저장
- 고유성을 효율적으로 보장하며, 추가, 삭제, 존재 여부 확인(in연산)이 데이터의
  크기에 상관없이 매우 빠르다.
- 합.교.차집합 등 수학적 집합연산을 간편하게 수행 가능

'''


# for idx, item in enumerate(data):
#     if all(key in item for key in key_list):
#         print(f"✅ index {idx}: 모든 key 존재")
#     else:
#         print(f"❌ index {idx}: 일부 key 없음 → 누락된 키: {[key for key in key_list if key not in item]}")