from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'navbar': 'home'})


def about(request):
    return render(request, 'about.html', {'navbar': 'about'})


def portfolio(request):
    return render(request, 'portfolio.html', {'navbar': 'portfolio'})


def contact(request):
    return render(request, 'contact.html', {'navbar': 'contact'})
