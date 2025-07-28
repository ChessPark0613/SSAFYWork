import requests
from pprint import pprint as print


dummy_data = []

for i in range(1, 11):
    # 무작위 유저 정보 요청 경로
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    # API 요청
    response = requests.get(API_URL)
    # JSON -> dict 데이터 변환
    parsed_data = response.json()

    companyName = parsed_data['company']['name']
    lat = float(parsed_data['address']['geo']['lat'])
    lng = float(parsed_data['address']['geo']['lng'])
    name = parsed_data['name']

    if lat >= 80 and lat <= -80 or lng >= 80 or lng <= -80:
        continue

    dummy_dict = {'company' : companyName,
                   'lat' : lat, 
                   'lng' : lng, 
                   'name' : name}

    dummy_data.append(dummy_dict)

print(dummy_data)


    
