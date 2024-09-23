
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages

from .models import DocumentDemande

User = get_user_model()


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte a été créé avec succès!')
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()

    return render(request, 'inscription.html', {'form': form})


def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('admin:index')
        else:
            return redirect('user_dashboard')
    return redirect('login')


@login_required
def user_dashboard(request):
    return render(request, 'user_page.html')


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Vous êtes connecté avec succès!')
                if user.is_superuser:
                    return redirect('admin:index')
                elif user.role == 'agent':
                    return redirect('agent_page')
                return redirect('user_dashboard')
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def demande_document(request):
    if request.method == 'POST':
        document_type = request.POST.get('document_type')
        if document_type == 'acte_naissance':

            nom_enfant = request.POST.get('nom_enfant')
            prenom_enfant = request.POST.get('prenom_enfant')
            date_naissance = request.POST.get('date_naissance')
            lieu_naissance = request.POST.get('lieu_naissance')
            nom_pere = request.POST.get('nom_pere')
            prenom_pere = request.POST.get('prenom_pere')
            nom_mere = request.POST.get('nom_mere')
            prenom_mere = request.POST.get('prenom_mere')

            DocumentDemande.objects.create(
                document_type=document_type,
                nom_enfant=nom_enfant,
                prenom_enfant=prenom_enfant,
                date_naissance=date_naissance,
                lieu_naissance=lieu_naissance,
                nom_pere=nom_pere,
                prenom_pere=prenom_pere,
                nom_mere=nom_mere,
                prenom_mere=prenom_mere,
                is_accepted=False
            )
        elif document_type == 'acte_mariage':

            nom_epoux = request.POST.get('nom_epoux')
            prenom_epoux = request.POST.get('prenom_epoux')
            nom_epouse = request.POST.get('nom_epouse')
            prenom_epouse = request.POST.get('prenom_epouse')
            nom_mariage = request.POST.get('nom_mariage')

            DocumentDemande.objects.create(
                document_type=document_type,
                nom_epoux=nom_epoux,
                prenom_epoux=prenom_epoux,
                nom_epouse=nom_epouse,
                prenom_epouse=prenom_epouse,
                nom_mariage=nom_mariage,
                is_accepted=False
            )
        return redirect('success_page')

    return render(request, 'demande_page.html')


def logout(request):
    return render(request, 'inscription.html')


def success_page(request):
    return render(request, 'demande_reussi.html')


def liste_demandes(request):
    # Récupérer toutes les demandes en attente
    demandes = DocumentDemande.objects.filter(status='en_attente')
    return render(request, 'agent_page.html', {'demandes': demandes})

def accepter_demande(request, demande_id):
    # Accepter une demande spécifique
    demande = get_object_or_404(DocumentDemande, id=demande_id)
    demande.status = 'acceptee'
    demande.save()
    return redirect('agent_page')

def refuser_demande(request, demande_id):
    # Refuser une demande spécifique
    demande = get_object_or_404(DocumentDemande, id=demande_id)
    demande.status = 'refusee'
    demande.save()
    return redirect('agent_page')

def affichedemande(request,demande_id):
    demande=get_object_or_404(DocumentDemande, id=demande_id)
    return render(request, 'demande_show.html', {'demande':demande})