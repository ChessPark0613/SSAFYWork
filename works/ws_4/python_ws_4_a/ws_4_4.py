import requests
from pprint import pprint as print

dummy_data = []

for i in range(1, 11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    response = requests.get(API_URL)
    parsed_data = response.json()

    companyName = parsed_data['company']['name']
    lat = float(parsed_data['address']['geo']['lat'])
    lng = float(parsed_data['address']['geo']['lng'])
    name = parsed_data['name']

    if lat >= 80 or lat <= -80 or lng >= 80 or lng <= -80:
        continue

    dummy_dict = {
        'company': companyName,
        'lat': lat,
        'lng': lng,
        'name': name
    }

    dummy_data.append(dummy_dict)

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

def censorship(company, name):
    if company in black_list:
        print(f'{company} 소속의 {name} 은/는 등록할 수 없습니다.')
        return False
    else:
        print(f'이상 없습니다.')
        return True

def create_user(user_list):
    censored_user_list = {}
    for user in user_list:
        company = user['company']
        name = user['name']

        if censorship(company, name):
            if company not in censored_user_list:
                censored_user_list[company] = []
            censored_user_list[company].append(name)
    
    return censored_user_list

result = create_user(dummy_data)
print(result)
