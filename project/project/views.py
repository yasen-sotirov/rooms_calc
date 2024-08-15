from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # http://localhost:8000/