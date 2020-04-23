from django import forms
from song.models import Geet

class GeetForm(forms.ModelForm):
	class Meta():
		model=Geet
		fields=('title','track','artist',)