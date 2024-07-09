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