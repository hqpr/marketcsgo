from django.shortcuts import render


def update(request):
    return render(request, 'update.html', {})

def insert(request):
    return render(request, 'insert.html', {})

def ping(request):
    return render(request, 'ping.html', {})
