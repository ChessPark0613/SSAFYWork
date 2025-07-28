# python_review_2025_07_28.py
# 📘 2025년 7월 28일 파이썬 학습 내용 정리

# ---------------------------
# ✅ 1. 리스트 메서드 정리
# ---------------------------

lst = [1, 2, 3]

lst.append(4)
print("append:", lst)  # [1, 2, 3, 4]

lst.extend([5, 6])
print("extend:", lst)  # [1, 2, 3, 4, 5, 6]

lst.insert(2, 99)
print("insert:", lst)  # [1, 2, 99, 3, 4, 5, 6]

lst.remove(99)
print("remove:", lst)  # [1, 2, 3, 4, 5, 6]

print("pop():", lst.pop())  # 6 (제거 및 반환)
print("pop(0):", lst.pop(0))  # 1
print("after pop:", lst)

lst.clear()
print("clear:", lst)  # []

lst = [10, 20, 30, 20]
print("index 20:", lst.index(20))         # 1
print("index 20 from 2:", lst.index(20, 2))  # 3

# ---------------------------
# ✅ 2. 가변 객체 vs 불변 객체
# ---------------------------

# 불변 객체: int, str, tuple 등
a = 100
print("a id before:", id(a))
a += 1
print("a id after :", id(a))  # id 변경됨 → 새로운 객체

s = "abc"
print("s id before:", id(s))
s += "def"
print("s id after :", id(s))  # id 변경됨

# 가변 객체: list, dict, set 등
l = [1, 2, 3]
print("list id before:", id(l))
l.append(4)
print("list id after :", id(l))  # id 유지됨

d = {"x": 1}
print("dict id before:", id(d))
d["y"] = 2
print("dict id after :", id(d))  # id 유지됨

# ---------------------------
# ✅ 3. 얕은 복사 vs 깊은 복사
# ---------------------------

import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

# 얕은 복사
print("original id:", id(original))
print("shallow id :", id(shallow))
print("original[0] id:", id(original[0]))
print("shallow[0]  id:", id(shallow[0]))  # 같은 주소 → 내부 객체는 공유됨

# 깊은 복사
print("deep id       :", id(deep))
print("deep[0] id    :", id(deep[0]))     # 다른 주소 → 내부 객체까지 복사

shallow[0][0] = 99
print("after shallow change:", original)  # 내부 객체도 같이 바뀜

deep[0][0] = 77
print("after deep change:", original)     # 원본 영향 없음

# ---------------------------
# ✅ 4. 중복 제거 함수
# ---------------------------

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))  # 순서 보존 + 중복 제거

print("remove_duplicates:", remove_duplicates([1, 2, 2, 3, 1, 4]))

# ---------------------------
# ✅ 5. 메서드 체이닝 (Method Chaining)
# ---------------------------

# 🔹 정의:
# 여러 메서드를 “.”으로 연결해서 한 줄로 연속 실행하는 기법
# 대부분의 경우 원본을 바꾸는 메서드는 None을 반환하므로 체이닝 불가
# 체이닝이 가능하려면 **각 메서드가 자기 자신 또는 새로운 값을 반환**해야 함

# 🔹 예시 1: 문자열 (가능)
s = "  hello world  "
result = s.strip().upper().replace("WORLD", "Python")
print("method chaining string:", result)  # HELLO Python

# 🔹 예시 2: 리스트 (불가능한 경우)
lst = [1, 2, 3]
# lst.append(4).reverse()  ❌ 오류 발생 → append()는 None 반환
# 해결 방법:
lst.append(4)
lst.reverse()
print("fixed list chaining:", lst)

# 🔹 예시 3: 체이닝이 가능한 사용자 정의 클래스 예시
class ChainList:
    def __init__(self, data=None):
        self.data = data if data else []

    def add(self, x):
        self.data.append(x)
        return self  # 자기 자신 반환

    def double(self):
        self.data = [x * 2 for x in self.data]
        return self

    def show(self):
        print("chain result:", self.data)
        return self

cl = ChainList().add(1).add(2).double().show()  # 체이닝 OK


# ---------------------------
# ✅ 6. 문자열 메서드 정리
# ---------------------------

s = "hello world PYTHON"

# 1. s.title() → 각 단어의 첫 글자를 대문자로
print("title():", s.title())  # 'Hello World Python'

# 2. s.capitalize() → 첫 글자만 대문자로, 나머지는 소문자로
print("capitalize():", s.capitalize())  # 'Hello world python'

# 3. s.upper() → 전체 대문자로
print("upper():", s.upper())  # 'HELLO WORLD PYTHON'

# 4. s.lower() → 전체 소문자로
print("lower():", s.lower())  # 'hello world python'

# 5. s.swapcase() → 대문자는 소문자로, 소문자는 대문자로
print("swapcase():", s.swapcase())  # 'HELLO WORLD python'

# 🔹 한글 문자열에도 일부 적용 가능
k = "파이썬 PYTHON"
print("한글 title():", k.title())      # '파이썬 Python'
print("한글 swapcase():", k.swapcase())  # '파이썬 python'

# 🔹 주의: 원본 문자열은 변경되지 않음 (문자열은 불변 객체)
print("원본 문자열:", s)




# 🔹 주의할 점:
# - 체이닝을 하려면 각 메서드가 객체 자체(self) 또는 값을 반환해야 함
# - list.append(), list.reverse() 등은 None을 반환하므로 직접 체이닝 불가
# - 중간 결과가 필요하면 변수로 나눠서 쓰는 것이 더 명확함

# ---------------------------
# ✅ 끝! 오늘 학습한 내용 정리
'''
1. 리스트 메서드 (append, extend, insert, remove, pop, clear, index)
2. 가변 객체 vs 불변 객체 (list vs int, str 등)
3. 얕은 복사 vs 깊은 복사 (copy, deepcopy, 메모리 주소 비교)
4. 중복 제거 함수 구현 (set, dict.fromkeys)
5. 메서드 체이닝 개념과 사용법, 주의할 점
'''
