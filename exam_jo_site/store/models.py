from django.db import models
from django.db.models import Sum, F
from django.urls import reverse
from django.conf import settings
from account.models import Utilisateur
from django.db.models.signals import pre_save
from django.dispatch import receiver

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
    
    def update_price(self, *args, **kwargs):
        # Mettez à jour le prix ici. Par exemple, si vous voulez doubler le prix :
        self.price = self.price * self.quantite
        super().save(*args, **kwargs)
    
    
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
    commande_ok = models.BooleanField(default=False)
    total = models.FloatField(default=0.0)
    
    
    def get_total(self):
        total = 0
        for article in self.commandearticle_set.all():
            total += article.produit.price * article.quantite
        return total
    
    def autre_commande(self):
        nouvelle_commande = Commandes.objects.create(utilisateur=self.user)
        return nouvelle_commande
    
    
    def __str__(self):
        return f"{self.utilisateur} {self.type}"
    


class CommandeArticle(models.Model):
    commande = models.ForeignKey(Commandes, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produits, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)
    price = models.FloatField(default=0.0)
    

    def save(self, *args, **kwargs):
        self.price = self.produit.price * self.quantite
        super().save(*args, **kwargs)
        
    
    def __str__(self):
        return f"user: {self.commande.utilisateur}/ produit: {self.produit.name}/ qt:{self.quantite}"


class Cart(models.Model):
    utilisateur = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    commandes = models.ManyToManyField(Commandes)
    numero_commande = models.IntegerField(default=1)
    commander = models.BooleanField(default=False)
    date_commande = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(default=0.0)
    
    
    def update_total(self):
        total = 0
        for commande in self.commandes.all():
            total += commande.get_total()
        self.total = total
        self.save()
        if total == 0.0:
            return "Gratuit"


    
    def __str__(self):
        return f"{self.utilisateur.username} -- #{self.numero_commande} -- {self.date_commande}"
    
    
    



