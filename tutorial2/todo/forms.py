from django import forms

class AgregarTarea(forms.Form):
	tarea = forms.CharField()