from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from goods.models import Categories

def index(request):

    context = {
        'title': 'Home - main',
        'content': 'Furniture store HOME',
    }
    return render(request,'main/index.html', context)

def about(request):

    context = {
        'title': 'Home - About as',
        'context': 'About as',
        'text_on_page': 'Text about why tish store is so cool',
    }

    return render(request,'main/about.html', context)
