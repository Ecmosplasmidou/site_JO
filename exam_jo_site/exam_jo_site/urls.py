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
from my_authentification import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("inscription/", views.inscription, name="inscription"),
    path("connexion/", views.connexion, name="connexion"),
    path("", views.accueil, name="accueil"),
    path("accueil2/", views.accueil2, name="accueil2"),
    path("deconnexion/", views.deconnexion, name="deconnexion"),
    path("billetterie/", views.billetterie, name='billetterie'),
    path("judo/", views.judo, name='judo'),
    path("checkout/", views.checkout, name='checkout'),
    path("erreur/", views.erreur, name='erreur'),
    path("search/", views.search_view, name='search_view'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
