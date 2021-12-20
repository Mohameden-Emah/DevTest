from django.db import models

# Create your models here.

class Consultation(models.Model):
        #nom du patient
        nom = models.CharField(max_length=50,default="")
        #prenom du patient
        prenom =  models.CharField(max_length=50,default="")
        #Date naissance du patient
        Date_Naissance = models.DateField(null=True, default="")
        #Sex patient
        sex =  models.CharField(max_length=6,default="")
        #Groupe saguin du patient
        groupe_Sanguin = models.CharField(max_length=3,default="")
        Date_Consultation = models.DateField(null=True, default="")
        Poids = models.FloatField(default="")
        Tension = models.CharField(max_length=20,default="")
        Taille = models.FloatField(default="")
        Observation = models.CharField(max_length=250,default="")

        def __str__(self) -> str:
            return super().__str__()

