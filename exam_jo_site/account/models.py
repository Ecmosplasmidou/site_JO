from django.db import models

# # Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UtilisateurManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, nom, prenom, username):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            nom=nom,
            prenom=prenom,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Utilisateur(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique= True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_inscription = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='images/', blank=True)
    
    is_staff = models.BooleanField(default=False)

    
    objects = UtilisateurManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nom', 'prenom']

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return self.username