from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    print('Home')

    return render(
        request,
        'home/index.html'
    )

