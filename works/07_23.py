# True False 반환
def is_negative(number):
    return number <= 0 # 3항식 없음 그냥 이렇게 바로 True || False 반환

# parameter 기본 값 설정 :: 매개변수(parameter), 인자(argument) 구분지어 생각하기
# 변수에 할당되는건 parm
# 변수 내부에서 사용하는건 argu
def default_arg_func(default = '기본 값'): # 기본 값 설정 방법 True && False && None 등 사용 가능
    return default


# ✅ 1. Arbitrary Argument Lists (*args)
# 위치 인자를 개수 제한 없이 튜플로 받는 방식

def add_all(*args):
    """
    임의의 개수의 숫자를 모두 더하는 함수
    *args는 튜플로 전달됨
    """
    return sum(args)

print("▶ add_all 예시")
print(add_all(1, 2, 3))           # 6
print(add_all(10, 20, 30, 40))    # 100
print()


# ✅ 2. Arbitrary Keyword Argument Lists (**kwargs)
# 키워드 인자를 개수 제한 없이 딕셔너리로 받는 방식

def print_info(**kwargs):
    """
    임의의 키워드 인자를 출력하는 함수
    **kwargs는 딕셔너리로 전달됨
    """
    print("▶ print_info 예시")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print()

print_info(name="정후", age=30)


# ✅ 3. *args와 **kwargs 함께 사용 예시

def example(pos1, *args, kw1='기본', **kwargs):
    """
    다양한 인자들을 조합해서 받는 함수
    - pos1: 위치 인자
    - *args: 임의의 위치 인자들
    - kw1: 기본값을 가진 키워드 인자
    - **kwargs: 임의의 키워드 인자들
    """
    print("▶ example 함수 호출 결과")
    print("pos1:", pos1)
    print("args:", args)
    print("kw1:", kw1)
    print("kwargs:", kwargs)
    print()

example(1, 2, 3, 4, kw1='변경', kw2='추가', kw3='더 추가')


# ✅ 요약 주석
"""
[정리 요약]

*args:
- 위치 인자를 개수 제한 없이 받을 때 사용
- 내부적으로 튜플(tuple)로 전달됨

**kwargs:
- 키워드 인자를 개수 제한 없이 받을 때 사용
- 내부적으로 딕셔너리(dict)로 전달됨

함수 정의 시 순서:
1. 일반 인자
2. *args
3. 기본값 인자
4. **kwargs
"""



name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

# list(map(lambda x: create_user(*x), zip(name, age, address)))



# ####################################################
number_of_book = 100
number_of_people = 0
user_infos = []


def increase_user():
    global number_of_people
    number_of_people += 1

def create_user(name, age, address):
    global user_infos
    increase_user()
    user_info = {
        'name': name,
        'age': age,
        'address': address,
    }
    user_infos.append(user_info)
    print(f'{name}님 환영합니다!')
    return user_info

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

for i in range(len(name)):
    create_user(name[i], age[i], address[i])


many_user = user_infos


def rental_book(info):
    count_book = info['age'] // 10
    decrease_book(count_book)
    print(f'남은 책의 수 : {number_of_book}')
    print(f'{info["name"]}님이 {count_book}권의 책을 대여하였습니다.')


def decrease_book(count_book):
    global number_of_book
    number_of_book -= count_book


rental_infos = list(map(lambda info: {'name': info['name'], 'age': info['age']}, many_user))
list(map(lambda info: rental_book(info), rental_infos))