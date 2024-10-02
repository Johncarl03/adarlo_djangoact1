from django.shortcuts import render

def home(request):
    return render(request, 'app2/home.html')

def page1(request):
    return render(request, 'app2/page1.html')

def page2(request):
    return render(request, 'app2/page2.html')
