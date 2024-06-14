from django.shortcuts import render, redirect
from .form import CustomerUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
import os

# Create your views here.

def inscription(request):
    if request.method == "POST":
        form = CustomerUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("connexion")
    else:
        form = CustomerUserCreationForm()
    return render(request, "inscription.html", {"form": form})

def connexion(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("accueil2")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
    return render(request, "connexion.html")


def accueil(request):    
    return render(request, "accueil.html")

def accueil2(request):
    return render(request, "accueil2.html")

def deconnexion(request):
    logout(request)
    return redirect("accueil")

def billetterie(request):   
    return render(request, "billetterie.html")

def judo(request):
    return render(request, "judo.html")

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
                    
            

# def search_suggestions(request):
#     dir_path = os.path.dirname(os.path.realpath(__file__))
#     templates_path = os.path.join(dir_path, 'templates')
#     all_files = os.listdir(templates_path)
#     html_files = [f for f in all_files if f.lower().endswith('.html')]
#     results = [f for f in html_files]

