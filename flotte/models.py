from django.db import models

# Create your models here.

class Modele(models.Model):
    nom_modele = models.CharField(max_length=100)
    marque = models.CharField(max_length=100)
    ESSENCE, DIESEL, ELECTRIQUE, HYBRIDE = 'Essence', 'Diesel', 'Électrique', 'Hybride'
    CARBURANT_CHOICES = [(ESSENCE, 'Essence'), (DIESEL, 'Diesel'), (ELECTRIQUE, 'Électrique'), (HYBRIDE, 'Hybride')]
    type_carburant = models.CharField(max_length=50, choices=CARBURANT_CHOICES, default=DIESEL)

    def __str__(self):
        return f"{self.marque} {self.nom_modele}"

class Vehicule(models.Model):
    immatriculation = models.CharField(max_length=20, unique=True)
    modele = models.ForeignKey(Modele, on_delete=models.CASCADE)
    kilometrage = models.IntegerField(default=0)
    EN_SERVICE, EN_REPARATION, HORS_USAGE = 'En service', 'En réparation', 'Hors d\'usage'
    ETAT_CHOICES = [(EN_SERVICE, 'En service'), (EN_REPARATION, 'En réparation'), (HORS_USAGE, 'Hors d\'usage')]
    etat = models.CharField(max_length=50, choices=ETAT_CHOICES, default=EN_SERVICE)
    date_fabrication = models.DateField()

    def __str__(self):
        return self.immatriculation

class Maintenance(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    type_intervention = models.CharField(max_length=200)
    date_derniere_revision = models.DateField()
    
    def __str__(self):
        return f"Maintenance {self.vehicule.immatriculation}"