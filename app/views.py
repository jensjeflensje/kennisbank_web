from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def support(request):
    return render(request, "support.html")
