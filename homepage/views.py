from django.shortcuts import render

def homepage(request):
    return render(request,"homepage\\about.html" )

def contacts(request):
    return render(request, "homepage\\numbers.html")

def operations(request):
    return render(request, "homepage\page.html")