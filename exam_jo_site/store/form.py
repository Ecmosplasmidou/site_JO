from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomerUserCreationForm(UserCreationForm):
    nom = forms.CharField(max_length=100,
                          label="Nom",
                          widget=forms.TextInput(attrs={'autocomplete': 'nom'}))

    prenom = forms.CharField(max_length=100,
                             label="Prénom",
                             widget=forms.TextInput(attrs={'autocomplete': 'prenom'}))
    
    password1 = forms.CharField(
                label="Mot de passe",
                strip=False, #sert à ne pas enlever les espaces autour de "mot de passe"
                widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'})
                                )
    
    password2 = forms.CharField(
                label="Confirmation du mot de passe",
                widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
                strip=False
                                )
    
    class Meta(UserCreationForm.Meta): #sert à créer les champs de formulaire
        fields = UserCreationForm.Meta.fields + ("nom", "prenom", "password1", "password2")