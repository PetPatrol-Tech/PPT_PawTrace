from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    context = {}
    context['hello']="welcome it"
    return render(request,'first.html',context)
