from django.shortcuts import render

def home(request):
    return render(request, 'app1/home.html')

def page1(request):
    return render(request, 'app1/page1.html')

def page2(request):
    return render(request, 'app1/page2.html')

