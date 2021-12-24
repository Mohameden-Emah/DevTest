from django.db import models

# Create your models here.

class Consultation(models.Model):
    SEX = (
        ('Homme', 'Homme'),
        ('Femme', 'Femme')
    )
    GROUPE_SANGUIN = (
        ('O+', 'O+'),
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('O-', 'O-'),
        ('A-', 'A-'),
        ('AB+', 'AB+'),
        ('B-', 'B-'),
        ('AB-', 'AB-')
    )

    #nom du patient
    nom = models.CharField(max_length=50,default="")
    #prenom du patient
    prenom =  models.CharField(max_length=50,default="")
    #Date naissance du patient
    Date_Naissance = models.DateField()
    #Sex patient
    sex =  models.CharField(max_length=6,default="", choices=SEX)
    #Groupe saguin du patient
    groupe_Sanguin = models.CharField(max_length=3,default="", choices=GROUPE_SANGUIN)
    #photo du profile
    profile_pic = models.ImageField(null=True, blank=True)
    Date_Consultation = models.DateField()
    Poids = models.FloatField(default="")
    Tension = models.CharField(max_length=20,default="")
    Taille = models.FloatField(default="")
    Observation = models.TextField(max_length=5000,default="")

    def __str__(self) -> str:
        return super().__str__()

