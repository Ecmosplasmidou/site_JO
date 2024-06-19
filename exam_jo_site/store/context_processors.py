from django.shortcuts import get_object_or_404
from .models import Cart, CommandeArticle
from django.db.models import Sum

def vue_panier(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(utilisateur=request.user) 
        panier = get_object_or_404(Cart, utilisateur=request.user)
        commandearticles = CommandeArticle.objects.filter(commande__in=panier.commandes.all())
        total_quantite, = cart.total_quantite()
        return {'commandes': panier.commandes.all(), 'commandearticles': commandearticles, 'cart': cart, 'total_quantite': total_quantite}
    return {}


def context_panier(request):
    total_quantite = 0
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(utilisateur=request.user)
        panier = get_object_or_404(Cart, utilisateur=request.user)
        total_quantite = CommandeArticle.objects.filter(commande__in=cart.commandes.all()).aggregate(Sum('quantite'))['quantite__sum'] or 0
        return {'commandes' : panier.commandes.all(),'total_quantite': total_quantite, 'cart': cart}
    return{}
