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