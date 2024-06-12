from django.db import models

# Create your models here.
class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    mot_de_passe = models.CharField(max_length=100)
    date_de_naissance = models.DateField()
    date_inscription = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='images/', blank=True)
