from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('AjoutConsultation/', views.AjoutConsultation, name='AjoutConsultation'),
    
]