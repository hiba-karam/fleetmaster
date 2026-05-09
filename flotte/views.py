from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehicule, Modele
from .forms import VehiculeForm
from datetime import date
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    vehicules = Vehicule.objects.all()
    modeles = Modele.objects.all()
    search_query = request.GET.get('search')
    etat_query = request.GET.get('etat')
    annee_query = request.GET.get('annee')
    modele_query = request.GET.get('modele') 
    if search_query:
        vehicules = vehicules.filter(immatriculation__icontains=search_query)
    if etat_query:
        vehicules = vehicules.filter(etat=etat_query)
    if annee_query: 
        vehicules = vehicules.filter(date_fabrication__year=annee_query)
    if modele_query:
        vehicules = vehicules.filter(modele__id=modele_query)
    vehicules = list(vehicules)
    for vehicule in vehicules:
        age = (date.today() - vehicule.date_fabrication).days / 365
        vehicule.est_ancien = age > 5
    return render(request, 'dashboard.html', {
        'vehicules': vehicules,
        'modeles': modeles
    })

def update_km(request, vehicule_id):
    if request.method == "POST":
        vehicule = get_object_or_404(Vehicule, id=vehicule_id)
        nouveau_km = int(request.POST.get('nouveau_km', 0))
        if nouveau_km >= 0:  
            vehicule.kilometrage = nouveau_km
            vehicule.save()
    return redirect('dashboard')

def ajouter_vehicule(request):
    if request.method == 'POST':
        form = VehiculeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = VehiculeForm()
    return render(request, 'ajouter_vehicule.html', {'form': form})

def modifier_vehicule(request, vehicule_id):
    vehicule = get_object_or_404(Vehicule, id=vehicule_id)
    if request.method == 'POST':
        form = VehiculeForm(request.POST, instance=vehicule)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = VehiculeForm(instance=vehicule)
    return render(request, 'modifier_vehicule.html', {'form': form, 'vehicule': vehicule})

def supprimer_vehicule(request, vehicule_id):
    vehicule = get_object_or_404(Vehicule, id=vehicule_id)
    if request.method == 'POST':
        vehicule.delete()
        return redirect('dashboard')
    return render(request, 'supprimer_vehicule.html', {'vehicule': vehicule})