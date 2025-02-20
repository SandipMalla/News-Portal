import requests
from django.shortcuts import render

API_KEY = "pub_705818f2f978752e41ef8aff6e2539c379521"

def fetch_news(request):
    API_URL = "https://newsdata.io/api/1/latest"
    q = request.GET.get('country')
    category = request.GET.get('category')
    API_URL += f"?q={q}&category={category}&apikey={API_KEY}"

    response = requests.get(API_URL)
    print(response.url)
    print(response.status_code)
    print(response.text)
    print(response.json().get('results'))
    news_data = response.json().get('results')

    return render(request, 'home.html', {'news': news_data})
