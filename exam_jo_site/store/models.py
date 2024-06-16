from django.db import models

# Create your models here.

class Produit(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100) #slug est un champ qui permet de créer des urls plus lisible
    description = models.TextField(blank=True) #blank=True rends la description facultative
    price = models.FloatField() #default=0.0 permet de mettre une valeur par défaut
    image = models.ImageField(upload_to='images/', blank=True, null=True) #null=True fait en sorte qu'on puisse mettre une valeur null dans la base de données
    
    def gratuit(self):
        if self.price == 0.0:
            return "Gratuit"
        else:
            return self.price
    
    def __str__(self):
        # first_line_description = self.description.split('\n')[0] #on prends la premiere ligne de descirption avec [0]
        return self.name
    
class Boxe_produit(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100) #slug est un champ qui permet de créer des urls plus lisible
    description = models.TextField(blank=True) #blank=True rends la description facultative
    price = models.FloatField() #default=0.0 permet de mettre une valeur par défaut
    image = models.ImageField(upload_to='images/', blank=True, null=True) #null=True fait en sorte qu'on puisse mettre une valeur null dans la base de données
    
    def gratuit(self):
        if self.price == 0.0:
            return "Gratuit"
        else:
            return self.price
    
    def __str__(self):
        # first_line_description = self.description.split('\n')[0] #on prends la premiere ligne de descirption avec [0]
        return self.name


class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    mot_de_passe = models.CharField(max_length=100)
    date_de_naissance = models.DateField()
    date_inscription = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='images/', blank=True)
    
    def __str__(self):
        return self.nom
