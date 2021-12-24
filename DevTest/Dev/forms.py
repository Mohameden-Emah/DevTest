from django import forms
from .models import Consultation

class CreatConsultation(forms.ModelForm):
	class Meta:
		model = Consultation
		fields = "__all__"