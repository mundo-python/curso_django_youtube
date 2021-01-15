from django.shortcuts import render
from django.http import HttpResponse


def moneda(request):
	num = 1
	context = {'num' : num}
	return render(request, 'hola/moneda.html', context)


def hola(request):
	return render(request, 'hola/index.html')

def saludo(request, nombre):
	context = {'name' : nombre}
	return render(request, 'hola/saludo.html', context)

