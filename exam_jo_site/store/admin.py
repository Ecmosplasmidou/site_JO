from django.contrib import admin
# from .models import Produit
# from .models import Boxe_produit
# from .models import Football_produit
# from .models import commande_judo
# from .models import commande_boxe_produit
# from .models import commande_football_produit
from .models import Cart
from .models import Commandes
from .models import Produits

# Register your models here.

# admin.site.register(Produit)
# admin.site.register(Boxe_produit)
# admin.site.register(Football_produit)
# admin.site.register(commande_judo)
# admin.site.register(commande_boxe_produit)
# admin.site.register(commande_football_produit)
admin.site.register(Commandes)
admin.site.register(Produits)
admin.site.register(Cart)
