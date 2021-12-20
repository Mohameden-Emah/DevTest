from django.shortcuts import render
from django.http import HttpResponse
from .models import Consultation
# Create your views here.
def home(request):
    Consult = Consultation.objects.all()
    return render(request, 'home.html', {'Consult' : Consult})

def AjoutConsultation(request):
    Consult = Consultation.objects.all()
    if request.method == 'POST' :
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        Date_Naissance = request.POST['Date_Naissance']
        sex = request.POST['sex']
        groupe_Sanguin = request.POST['groupe_Sanguin']
        Date_Consultation = request.POST['Date_Consultation']
        Poids = request.POST['Poids']
        Tension = request.POST['Tension']
        Taille = request.POST['Taille']
        Observation = request.POST['Observation']
        
        consultation = Consultation.objects.create(
            nom=nom,
            prenom=prenom,
            Date_Naissance=Date_Naissance,
            sex=sex,
            groupe_Sanguin=groupe_Sanguin,
            Date_Consultation=Date_Consultation,
            Poids=Poids,
            Tension=Tension,
            Taille=Taille,
            Observation=Observation
        )

    return render(request, 'AjoutConsultation.html', {'Consult ' : Consult})

   
