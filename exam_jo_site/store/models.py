from django.db import models
from django.urls import reverse
from django.conf import settings
from account.models import Utilisateur

# Create your models here.

class Produits(models.Model):
    TYPE_CHOICES = [
        ('judo', 'Judo'),
        ('boxe', 'Boxe'),
        ('football', 'Football'),
        # Ajoutez d'autres types de produits ici
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100) 
    description = models.TextField(blank=True) 
    quantite = models.IntegerField(default=1)
    price = models.FloatField() 
    image = models.ImageField(upload_to='images/', blank=True, null=True) 
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)  # Nouveau champ

    def gratuit(self):
        if self.price == 0.0:
            return "Gratuit"
        else:
            return self.price
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"/{self.type}/{self.slug}/"  # Utilisez self.type ici
    
    
class Commandes(models.Model):
    TYPE_CHOICES = [
        ('judo', 'Judo'),
        ('boxe', 'Boxe'),
        ('football', 'Football'),
        # Ajoutez d'autres types de produits ici
    ]

    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    produits = models.ManyToManyField(Produits, through='CommandeArticle')
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.utilisateur} {self.type}"
    

class CommandeArticle(models.Model):
    commande = models.ForeignKey(Commandes, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produits, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"user: {self.commande.utilisateur}/ produit: {self.produit.name}/ qt:{self.quantite}"


class Cart(models.Model):
    utilisateur = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    commandes = models.ManyToManyField(Commandes)
    # commandes_boxe = models.ManyToManyField(commande_boxe_produit)
    # commandes_football = models.ManyToManyField(commande_football_produit)
    numero_commande = models.IntegerField(default=1)
    commander = models.BooleanField(default=False)
    date_commande = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.utilisateur.username} -- #{self.numero_commande} -- {self.date_commande}"


