import logging

from django.http import HttpResponse
from django.shortcuts import render, redirect
from Residents.models import Resident
from Incident.models import Incident
from Images.models import Images
from Pets.models import Pet
from Incident.models import Incident
from Residents.models import Resident
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
    all = Pet.objects.all()
    return render(request, 'option2.html',{"pets":all})


def option3(request):
    all = Incident.objects.all()
    return render(request, 'option3.html', {"incidents": all})


def login(request):
    return render(request, "login.html")


def option4(request):
    incident_number = request.GET.get('incident_number')
    print(incident_number)
    image = []
    ans = Images.objects.get(Incident_number_id=incident_number)
    print(ans)
    image.append(ans)
    return render(request, 'option4.html', {'images': image})
def refresh_state(request):
    incidents_list=Incident.objects.filter(status=2)
    for incident in incidents_list:
        print("--------------------------------------------")
        print(incident.resident_id)
        resident_list=Resident.objects.filter(id=incident.resident_id)
        incident_number=incident.incident_number
        for resident in resident_list:
            resident.state-=5
            resident.save()
            Incident.objects.filter(incident_number=incident_number).delete()
    return redirect('option1')

def update_status(request):
    if request.method == 'POST':
        incident_id = request.POST.get('Incidentid')
        incident_id =int(incident_id[9:])
        test = request.POST.get('optradio')


        if(test=="option1"):
            try:
                incident = Incident.objects.get(incident_number=incident_id)
                incident.status = 2
                incident.save()
            except Incident.DoesNotExist:
                return HttpResponse("Incident does not exist", status=404)
    return redirect('option3')