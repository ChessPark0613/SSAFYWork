from django.shortcuts import render
import requests

API_URL = "http://www.aladin.co.kr/ttb/api/ItemList.aspx"
API_KEY = "ttbqh6131006001"

def book_info():
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
                "isbn": b["isbn"],
                "author": b["author"],
                "title": b["title"],
                "pubDate": b["pubDate"]
            })
        return res


    if response.status_code == 200:
        data = response.json()
        return book_info(data['item'])
    else:
        return 
    
# Create your views here.
def index(request):
    context = {'book_info': book_info()}
    return render(request, 'index.html', context)