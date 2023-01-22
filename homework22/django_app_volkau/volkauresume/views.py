from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'volkauresume/home.html')

def education(request):
    return render(request, 'volkauresume/education.html')

def skills(request):
    return render(request, 'volkauresume/skills.html')

def aboutme(request):
    return render(request, 'volkauresume/aboutme.html')

