from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(requests):
    return render(requests, 'index.html')


def base(requests):
    return render(requests, 'base.html')

def shop(requests):
    return render(requests,'shop.html')