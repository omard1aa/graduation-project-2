from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'Home/home_page.html')

def initial(request):
    return HttpResponse("initial")