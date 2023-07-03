from django.shortcuts import render, redirect
from django.views import View
from .models import Edificio, Departamento
from .forms import EdificioForm, DepartamentoForm


def listar_edificios(request):
    edificios = Edificio.objects.all()

    informacion_template = {
        'items': edificios, 'numero_registros': len(edificios)}
    return render(request, 'edificios_list.html', informacion_template)


def listar_departamentos(request):
    departamentos = Departamento.objects.all()

    data = getDataForHtml(departamentos, len(departamentos))
    return render(request, 'edificios_list.html', data)


def getDataForHtml(items, numero_registros):
    return {'items': items, 'numero_registros': numero_registros}


def crear_edificio(request):
    if request.method == 'POST':
        form = EdificioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_edificios')
    else:
        form = EdificioForm()
    return render(request, 'edificios_form.html', {'form': form})


def crear_departamento(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_departamentos')
    else:
        form = DepartamentoForm()
    return render(request, 'edificios_form.html', {'form': form})


def editar_departamento(request, id):
    departamento = Departamento.objects.get(pk=id)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)
        
        if form.is_valid():
            form.save()
            return redirect(listar_departamentos)
    else:
        form = DepartamentoForm(instance=departamento)
    
    return render(request, 'edificios_form.html', {'form': form})


def editar_edificio(request, id):
    edificio = Edificio.objects.get(pk=id)
    if request.method == 'POST':
        form = EdificioForm(request.POST, instance=edificio)
        
        if form.is_valid():
            form.save()
            return redirect(listar_edificios)
    else:
        form = EdificioForm(instance=edificio)
    
    return render(request, 'edificios_form.html', {'form': form})