"""
URL configuration for fleetmaster project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from flotte import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('update_km/<int:vehicule_id>/', views.update_km, name='update_km'),
    path('ajouter/', views.ajouter_vehicule, name='ajouter_vehicule'),
    path('modifier/<int:vehicule_id>/', views.modifier_vehicule, name='modifier_vehicule'),
    path('supprimer/<int:vehicule_id>/', views.supprimer_vehicule, name='supprimer_vehicule'),
]
