import requests
from django.shortcuts import render

API_URL = 'https://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'ttbqh6131006001'

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    return get_info(request)

def bestseller(request):
    return get_info(request)

def get_info(request):
    segment = request.path.strip("/").split("/")[1]
    Target = {'recommend' : 'ItemNewSpecial', 'bestseller': 'Bestseller'}
    params = {
        'ttbkey': API_KEY,
        'QueryType': Target.get(segment),
        'MaxResults': '50',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

    response = requests.get(API_URL, params=params).json()

    result = []
    for item in response['item']:
        info = {
            'isbn': item['isbn'],
            'title': item['title'],
            'pubDate': item['pubDate'],
            'author': item['author'],
            'description': item['description'],
        }
        result.append(info)
    context = {
        'result': result
    }
    return render(request, f'{segment}.html', context)