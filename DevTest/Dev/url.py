from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('AjoutConsultation/', views.AjoutConsultation, name='AjoutConsultation'),
    path('Update/<int:id>/', views.Update, name='Update'),
    path('Delete/<int:id>/', views.Delete, name='Delete'),
]