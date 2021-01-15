from django.shortcuts import render, redirect
from .forms import AgregarTarea

tareas = []

def home(request):
	context = {'tareas' : tareas}
	return render(request, "todo/home.html", context)

def add(request):
	if request.method == 'POST':
		form = AgregarTarea(request.POST)
		if form.is_valid():
			tarea = form.cleaned_data["tarea"]
			tareas.append(tarea)
			return redirect('home')
		
	else: 
		form = AgregarTarea()

	context = {'form' : form}
	return render(request, "todo/add.html", context)

