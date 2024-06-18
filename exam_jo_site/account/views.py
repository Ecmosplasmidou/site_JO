from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomerUserCreationForm

# Create your views here.

def inscription(request):
    if request.method == "POST":
        form = CustomerUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("connexion")
        else:
            messages.error(request, "Champ incorrecte")
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
            return redirect("accueil")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
    return render(request, "connexion.html")

def deconnexion(request):
    logout(request)
    return redirect("accueil")