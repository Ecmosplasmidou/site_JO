from django.db import models
from django.urls import reverse
from django.conf import settings
from account.models import Utilisateur

# Create your models here.

# class Produit(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(max_length=100) #slug est un champ qui permet de créer des urls plus lisible
#     description = models.TextField(blank=True) #blank=True rends la description facultative
#     price = models.FloatField() #default=0.0 permet de mettre une valeur par défaut
#     image = models.ImageField(upload_to='images/', blank=True, null=True) #null=True fait en sorte qu'on puisse mettre une valeur null dans la base de données
    
#     def gratuit(self):
#         if self.price == 0.0:
#             return "Gratuit"
#         else:
#             return self.price
    
#     def __str__(self):
#         # first_line_description = self.description.split('\n')[0] #on prends la premiere ligne de descirption avec [0]
#         return self.name
    
#     def get_absolute_url(self):
#         return f"/judo/{self.slug}/"
    
# class Boxe_produit(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(max_length=100) #slug est un champ qui permet de créer des urls plus lisible
#     description = models.TextField(blank=True) #blank=True rends la description facultative
#     price = models.FloatField() #default=0.0 permet de mettre une valeur par défaut
#     image = models.ImageField(upload_to='images/', blank=True, null=True) #null=True fait en sorte qu'on puisse mettre une valeur null dans la base de données
    
#     def gratuit(self):
#         if self.price == 0.0:
#             return "Gratuit"
#         else:
#             return self.price
    
#     def __str__(self):
#         # first_line_description = self.description.split('\n')[0] #on prends la premiere ligne de descirption avec [0]
#         return self.name
    
#     def get_absolute_url(self):
#         return f"/boxe/{self.slug}/"

# class Football_produit(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(max_length=100) #slug est un champ qui permet de créer des urls plus lisible
#     description = models.TextField(blank=True) #blank=True rends la description facultative
#     price = models.FloatField() #default=0.0 permet de mettre une valeur par défaut
#     image = models.ImageField(upload_to='images/', blank=True, null=True) #null=True fait en sorte qu'on puisse mettre une valeur null dans la base de données
    
#     def gratuit(self):
#         if self.price == 0.0:
#             return "Gratuit"
#         else:
#             return self.price
    
#     def __str__(self):
#         # first_line_description = self.description.split('\n')[0] #on prends la premiere ligne de descirption avec [0]
#         return self.name
    
#     def get_absolute_url(self):
#         # return f"/football/{self.slug}/
#         return f"/football/{self.slug}/"

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
    
    
# class commande_judo(models.Model):
#     utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
#     quantite = models.IntegerField(default=1)
#     commande = models.BooleanField(default=False)
    
#     def __str__(self):
#         return f"{self.produit.name} {self.quantite}"
    
# class commande_boxe_produit(models.Model):
#     utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     produit = models.ForeignKey(Boxe_produit, on_delete=models.CASCADE)
#     quantite = models.IntegerField(default=1)
#     commande = models.BooleanField(default=False)
    
#     def __str__(self):
#         return f"{self.produit.name} {self.quantite}"

# class commande_football_produit(models.Model):
#     utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     produit = models.ForeignKey(Football_produit, on_delete=models.CASCADE)
#     quantite = models.IntegerField(default=1)
#     commande = models.BooleanField(default=False)
    
#     def __str__(self):
#         return f"{self.produit.name} {self.quantite}"
    
    
class Commandes(models.Model):
    TYPE_CHOICES = [
        ('judo', 'Judo'),
        ('boxe', 'Boxe'),
        ('football', 'Football'),
        # Ajoutez d'autres types de produits ici
    ]

    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produits, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)
    commande = models.BooleanField(default=False)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)  # Nouveau champ

    def __str__(self):
        return f"{self.produit.name} {self.quantite}"


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


