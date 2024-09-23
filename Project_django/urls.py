"""
URL configuration for Project_django project.

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
from django.urls import path
from Digital_doc import views


urlpatterns = [
    path('demande-document/', views.demande_document, name='demander_document'),
    path('admin/', admin.site.urls,name='admin'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('', views.register, name='index'),
    path('logout/', views.logout,name='logout'),
    path('success/', views.success_page, name='success_page'),
    path('demande//<int:demande_id>', views.affichedemande, name='affichedemande'),
    path('demandes/', views.liste_demandes, name='agent_page'),
    path('demandes/accepter/<int:demande_id>/', views.accepter_demande, name='accepter_demande'),
    path('demandes/refuser/<int:demande_id>/', views.refuser_demande, name='refuser_demande'),
]





