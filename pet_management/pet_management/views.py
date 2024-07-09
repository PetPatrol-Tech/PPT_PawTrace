from django.http import HttpResponse
from django.shortcuts import render
from Residents.models import Resident
def hello(request):
    context = {}
    context['hello']="welcome it"
    return render(request,'first.html',context)


def information(request):
    all=Resident.objects.all()
    return render(request,'table.html',{'all':all})

def option(request):
    return render(request, 'base.html')

def option1(request):
    all=Resident.objects.all()
    return render(request, 'options.html',{'all':all})

def option2(request):
    return render(request, 'option2.html')

def option3(request):
    return render(request, 'myapp/option3.html')