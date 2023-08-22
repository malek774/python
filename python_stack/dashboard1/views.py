from django.shortcuts import render

def index(request):
    return render(request, 'dashboard.html')

def book_list(request):
    return render(request, 'book_list.html')