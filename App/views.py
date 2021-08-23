from django.shortcuts import render
import requests
from django.core.paginator import Paginator

API_KEY = '0e7f3d4f9f9842969da8ff629ceb3b9b'

def home_View(request):
    if request.GET.get('country') is None and request.GET.get('language') is None and request.GET.get('category') is None:
        url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey={}'.format(API_KEY)
        res = requests.get(url)
        data = res.json()
        return render(request, 'home.html', {'data': data})
    elif request.GET.get('country'):
        country = request.GET.get('country')
        url = 'https://newsapi.org/v2/top-headlines?country={}&apiKey={}'.format(country ,API_KEY)
        res = requests.get(url)
        data = res.json()
        return render(request, 'home.html', {'data': data})
    elif request.GET.get('language'):
        language = request.GET.get('language')
        url = 'https://newsapi.org/v2/top-headlines?language={}&apiKey={}'.format(language ,API_KEY)
        res = requests.get(url)
        data = res.json()
        return render(request, 'home.html', {'data': data})
    elif request.GET.get('category'):
        category = request.GET.get('category')
        url = 'https://newsapi.org/v2/top-headlines?category={}&apiKey={}'.format(category ,API_KEY)
        res = requests.get(url)
        data = res.json()
        return render(request, 'home.html', {'data': data})
    
    



