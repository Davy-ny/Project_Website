from django.shortcuts import render, redirect
from .models import Tree


def indexPage(request):
    return render(request, 'index.html')


def contactPage(request):
    return render(request, 'contact.html')


def categoryPage(request):
    return render(request, 'category.html')


def registerPage(request):
    return render(request, 'register.html')

def formPage(request):
    return render(request, 'form.html')


def recordData(request):
    if request.method == 'POST':
        species = request.POST.get('species')
        handler = request.POST.get('handler')
        number = request.POST.get('number')
        date = request.POST.get('date')

        mine = Tree(species=species, handler=handler, number=number, date=date)
        mine.save()
        return redirect("/")
    return render(request, 'form.html')


def displayData(request):
    data = Tree.objects.all()
    context = {"data": data}
    return render(request, 'form.html', context)


def deleteData(request, id):
    d = Tree.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, 'form.html')


def updateData(request, id):
    if request.method == 'POST':
        species = request.POST.get('species')
        handler = request.POST.get('handler')
        number = request.POST.get('number')
        date = request.POST.get('date')

        stuff = Tree.objects.get(id=id)
        stuff.species = species
        stuff.handler = handler
        stuff.number = number
        stuff.date = date
        stuff.save()
        return redirect("/")
    plant = Tree.objects.get(id=id)
    context = {"plant": plant}
    return render(request, 'edit.html', context)
