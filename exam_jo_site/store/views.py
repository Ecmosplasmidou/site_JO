from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .forms import CustomerUserCreationForm
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.http import JsonResponse
# from difflib import get_close_matches
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.views.generic import TemplateView
from django.http import JsonResponse
import os


from store.models import Produits, Cart, Commandes, CommandeArticle

# # Create your views here.

def accueil(request):    
    return render(request, "accueil.html")

def accueil2(request):
    return render(request, "accueil2.html")

def billetterie(request):   
    return render(request, "billetterie.html")

def judo(request):
    produits = Produits.objects.filter(type='judo')
    return render(request, "judo.html", context={"produits": produits})

def boxe(request):
    produits = Produits.objects.filter(type='boxe')
    return render(request, "boxe.html", context={"produits": produits})

def football(request):
    produits = Produits.objects.filter(type='football')
    return render(request, "football.html", context={"produits": produits})


def produit_details(request, type, slug):
    produit = get_object_or_404(Produits, type=type, slug=slug)
    return render(request, "details.html", context={"produit": produit})


def add_to_cart(request, slug, type):
    utilisateur = request.user
    cart, created = Cart.objects.get_or_create(utilisateur=request.user) 
    print(f"Panier: {cart.id}, Commandes: {cart.commandes.count()}")
    panier, _ = Cart.objects.get_or_create(utilisateur=utilisateur)

    # Vérifiez si le type de produit est valide
    if type not in ['judo', 'boxe', 'football']:
        return HttpResponse('Invalid product type')

    # Obtenez le produit en fonction du slug et du type
    produit = get_object_or_404(Produits, slug=slug, type=type)

    # Obtenez la commande pour l'utilisateur actuel et le type de produit
    commande, _ = Commandes.objects.get_or_create(utilisateur=utilisateur, type=type)

    # Vérifiez si le produit est déjà dans la commande
    commande_article, created = CommandeArticle.objects.get_or_create(commande=commande, produit=produit)

    if created:
        # Si le produit n'était pas dans la commande, ajoutez-le au panier
        panier.commandes.add(commande)
        panier.save()
    else:
        # Si le produit était déjà dans la commande, augmentez la quantité
        commande_article.quantite += 1
        commande_article.save()
    panier.update_total()
    print(f'Updated cart total: {panier.total}')  # Ajoutez cette ligne
    return redirect('produit_details', slug=slug, type=type)



def panier(request):
    cart = Cart.objects.get(utilisateur=request.user) 
    panier = get_object_or_404(Cart, utilisateur=request.user)
    commandearticles = CommandeArticle.objects.filter(commande__in=panier.commandes.all())
    return render(request, "panier.html", context={"commandes": panier.commandes.all(), 'commandearticles': commandearticles, 'cart': cart})

# def vue_panier(request):
#     panier = get_object_or_404(Cart, utilisateur=request.user)
#     return render(request, "header3.html", context={"commandes": panier.commandes.all()})


def supr_panier(request, commande_id, commandearticle_id):
    commande = get_object_or_404(Commandes, id=commande_id, utilisateur=request.user)
    commande_article = get_object_or_404(CommandeArticle, id=commandearticle_id, commande_id=commande_id)
    if commande_article.quantite > 1:
        commande_article.quantite -= 1
        commande_article.save()
    else:
        commande_article.delete()
        if not CommandeArticle.objects.filter(commande=commande).exists():
            commande.delete()
    panier = get_object_or_404(Cart, utilisateur=request.user)
    panier.update_total()
    return redirect('panier')


def supr_panier_header(request, commande_id, commandearticle_id):
    commande = get_object_or_404(Commandes, id=commande_id, utilisateur=request.user)
    commande_article = get_object_or_404(CommandeArticle, id=commandearticle_id, commande_id=commande_id)
    if commande_article.quantite > 1:
        commande_article.quantite -= 1
        commande_article.save()
    else:
        commande_article.delete()
        if not CommandeArticle.objects.filter(commande=commande).exists():
            commande.delete()
    panier = get_object_or_404(Cart, utilisateur=request.user)
    panier.update_total()
    return redirect(request.META.get('HTTP_REFERER', 'default_if_none'))


def augmenter_panier(request, commandearticle_id):
    commandearticle = get_object_or_404(CommandeArticle, id=commandearticle_id)
    commandearticle.quantite += 1
    commandearticle.save()
    panier = get_object_or_404(Cart, utilisateur=request.user)
    panier.update_total()
    return redirect('panier')


def augmenter_panier_header(request, commandearticle_id):
    commandearticle = get_object_or_404(CommandeArticle, id=commandearticle_id)
    commandearticle.quantite += 1
    commandearticle.save()
    panier = get_object_or_404(Cart, utilisateur=request.user)
    panier.update_total()
    return redirect(request.META.get('HTTP_REFERER', 'default_if_none'))


def maj_prix(request, produit_id):
    commandearticle = get_object_or_404(CommandeArticle, id=produit_id)
    commandearticle.quantite += 1
    commandearticle.save()
    panier = get_object_or_404(Cart, utilisateur=request.user)
    panier.update_total()
    return redirect('panier')


def checkout(request):
    return render(request, "checkout.html")

def erreur(request):
    return render(request, "erreur.html")
        
def search_view(request):
    query = request.GET.get('recherche')
    results = []
    redirect_page = None
    
    if query:
        # return JsonResponse(request, "search_results.html", {"query": query, "results": results})
    
        query = query.lower()
    # Effectuez votre recherche sur plusieurs vues ou modèles ici
    # Obtenez le chemin absolu du répertoire contenant ce fichier
        dir_path = os.path.dirname(os.path.realpath(__file__))
            
            # Construisez le chemin du dossier 'templates'
        templates_path = os.path.join(dir_path, 'templates')
            
            # Liste tous les fichiers dans le dossier 'templates'
        all_files = os.listdir(templates_path)
            
            # Filtre la liste pour ne garder que les fichiers .html
        html_files = [f for f in all_files if f.lower().endswith('.html')]
            
            # Filtre la liste pour ne garder que les fichiers qui contiennent la requête de recherche
        results = [f for f in html_files if query in f.lower()]
            
            # # Si la recherche correspond à un fichier spécifique, redirigez vers cette page
        if 'accueil.html' in results:
                return redirect('accueil')
        elif 'billetterie.html' in results:
                return redirect('billetterie')
        elif 'accueil2.html' in results:
                return redirect('accueil2')
            # #mettre le reste des pages pour les recherches quand elle seront créees
            
            
        if f"{query}.html" in html_files:
            redirect_page = query
        
        # Sinon, renvoyez les résultats de la recherche
    if redirect_page:
            return redirect(redirect_page)
        #changer cette page par page d'erreur de recherche plus tard
    else:
        return render(request, "erreur.html", {"query": query})  

