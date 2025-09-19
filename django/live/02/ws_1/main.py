import requests
import pprint
print = pprint.pprint

API_URL = "http://www.aladin.co.kr/ttb/api/ItemList.aspx"
API_KEY = "ttbqh6131006001"
params = {
    'TTBKey': API_KEY,
    'QueryType': 'ItemNewSpecial',
    'SearchTarget': 'Book',
    'Start': 1,
    'MaxResults': 50,
    'Output': 'JS',
    'Version': '20131101'
}

response = requests.get(API_URL, params=params)

def book_info(items):
    res = []
    for b in items:
        res.append({
            "국제 표준 도서 번호": b["isbn"],
            "저자": b["author"],
            "제목": b["title"],
            "출간일": b["pubDate"]
        })
    return res


if response.status_code == 200:
    data = response.json()
    print(book_info(data['item']))
else:
    print("Request failed:", response.text)