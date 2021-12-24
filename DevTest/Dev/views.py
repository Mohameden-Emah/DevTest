from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Consultation
from .forms import CreatConsultation
# Create your views here.
def home(request):
    Consult = Consultation.objects.all()
    return render(request, 'home.html', {'Consult' : Consult})

def AjoutConsultation(request):
    form = CreatConsultation()
    if request.method == "POST":
        print(request.POST)
        form = CreatConsultation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form' : form}        
    return render(request, 'AjoutConsultation.html', context)


def Update(request, id):
    updateCons = Consultation.objects.get(pk=id)
    form = CreatConsultation(instance=updateCons)
    if request.method == "POST":
        
        form = CreatConsultation(request.POST, instance=updateCons)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form' : form}
    return render(request, 'AjoutConsultation.html', context)


def Delete(request, id):
    deletCons = Consultation.objects.get(pk=id)
    if request.method == "POST":
        deletCons.delete()
        return redirect('/')

    context = {'deletCons' : deletCons}
    return render(request, 'Delete.html', context)    
   
