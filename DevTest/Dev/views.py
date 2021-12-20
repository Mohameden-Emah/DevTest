from django.shortcuts import render
from django.http import HttpResponse
from .models import Consultation
# Create your views here.
def home(request):
    Consult = Consultation.objects.all()
    return render(request, 'home.html', {'Consult' : Consult})

def AjoutConsultation(request):
    # nom = request.POST['nom']
    # prenom = request.POST['prenom']
    # Date_Naissance = request.POST['Date_Naissance']
    # sex = request.POST['sex']
    # groupe_Sanguin = request.POST['groupe_Sanguin']
    # Date_Consultation = request.POST['Date_Consultation']
    # poids = request.POST['poids']
    # Tension = request.POST['Tension']
    # Taille = request.POST['Taille']
    # Observation = request.POST['Observation']

    return render(request, 'AjoutConsultation.html')
   
