from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def firstpage(request):
    return render(request,'firstpage.html')

def secpage(request):
    return render(request,'secpage.html')

def third(request):
    return HttpResponse('Hello first String ')

def fourth(request):
    return HttpResponse('Hello Second String')
