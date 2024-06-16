from django.contrib import admin
from .models import Produit
from .models import Boxe_produit

# Register your models here.

admin.site.register(Produit)
admin.site.register(Boxe_produit)
