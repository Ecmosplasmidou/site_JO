"""
URL configuration for exam_jo_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from store import views
from django.conf import settings
from django.conf.urls.static import static
# from store.views import produit_details
from account.views import inscription, connexion, deconnexion
from store.views import add_to_cart


urlpatterns = [
    path("admin/", admin.site.urls),
    path("inscription/", inscription, name="inscription"),
    path("connexion/", connexion, name="connexion"),
    path("", views.accueil, name="accueil"),
    path("accueil/", views.accueil, name="accueil"),
    path("accueil2/", views.accueil2, name="accueil2"),
    path("deconnexion/", deconnexion, name="deconnexion"),
    path("billetterie/", views.billetterie, name='billetterie'),
    # path('supr_panier/<int:commande_id>/', views.supr_panier, name='supr_panier'),
    path('augmenter_panier/<int:commandearticle_id>/', views.augmenter_panier, name='augmenter_panier'),
    path('augmenter_panier_header/<int:commandearticle_id>/', views.augmenter_panier_header, name='augmenter_panier_header'),
    path('supr_panier/<int:commande_id>/<int:commandearticle_id>/', views.supr_panier, name='supr_panier'),
    path('supr_panier_header/<int:commande_id>/<int:commandearticle_id>/', views.supr_panier_header, name='supr_panier_header'),
    path('<str:type>/<str:slug>/', views.produit_details, name='produit_details'),
    path('<str:type>/<str:slug>/add_to_cart', views.add_to_cart, name='add_to_cart'),
    path("judo/", views.judo, name='judo'),
    path("boxe/", views.boxe, name='boxe'),
    path("football/", views.football, name='football'),
    path("panier/", views.panier, name='panier'),
    path("success/", views.success, name='success'),
    path("failed/", views.failed, name='failed'),
    path("erreur/", views.erreur, name='erreur'),
    path("search/", views.search_view, name='search_view'),
    path("mes_commandes/", views.mes_commandes, name='mes_commandes'),
    path("conditions_genérales_de_vente/", views.CGV, name='CGV'),
    path("conditions_genérales_utilisation/", views.CGU, name='CGU'),
    path("mentions_legales/", views.ML, name='ML'),
    path("politique_de_confidentialite/", views.PDC, name='PDC'),
    path('generate_qr/', views.generate_qr, name='generate_qr'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
