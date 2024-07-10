from django.shortcuts import get_object_or_404, render
from Residents.models import Resident
from Incident.models import Incident
from Images.models import Images


def hello(request):
    context = {}
    context['hello'] = "welcome it"
    return render(request, 'first.html', context)


def information(request):
    all = Resident.objects.all()
    return render(request, 'table.html', {'all': all})


def option(request):
    return render(request, 'base.html')


def option1(request):
    all = Resident.objects.all()
    return render(request, 'options.html', {'all': all})


def option2(request):
    return render(request, 'option2.html')


def option3(request):
    all = Incident.objects.all()
    return render(request, 'option3.html', {"incidents": all})


def login(request):
    return render(request, "login.html")


def option4(request):
    incident_number = request.GET.get('incident_number')
    image=[]
    image.append(Images.objects.filter(Incident_number_id=incident_number))
    return render(request, 'option4.html', {'images': image})
