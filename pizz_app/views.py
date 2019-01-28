from django.shortcuts import render

def index(request):
    return render(request, 'pizz_app/index.html')
