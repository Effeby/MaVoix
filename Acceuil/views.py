from django.shortcuts import render





# Create your views here.

def index(request):
    datas = {}

    return render(request, "index.html", datas)

def login(request):
    datas = {}

    return render(request, "login.html", datas)

def register(request):
    datas = {}

    return render(request, "register.html", datas)

def main(request):
    datas = {}

    return render(request, "main.html", datas)


def info(request):
    datas = {}

    return render(request, "info.html", datas)

