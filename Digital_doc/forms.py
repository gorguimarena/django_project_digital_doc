from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Citoyen

User = get_user_model()


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
        'required': True,
    }), label='Email')

    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your username',
        'class': 'form-control'
    }), label='Nom d\'utilisateur')

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
    }), label='Password')

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
    }), label='Confirm Password')

    nom = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your name',
        'class': 'form-control'
    }), label='Nom')

    prenom = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your first name',
        'class': 'form-control'
    }), label='Prénom')

    lieu_naissance = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your place of birth',
        'class': 'form-control'
    }), label='Lieu de naissance')

    telephone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your phone number',
        'class': 'form-control'
    }), label='Téléphone')

    date_naissance = forms.DateField(required=True, widget=forms.DateInput(attrs={
        'placeholder': 'Enter your birth date',
        'class': 'form-control',
        'type': 'date'
    }), label='Date de naissance')

    class Meta:
        model = User  # Utilise le modèle d'utilisateur personnalisé
        fields = ['username', 'email', 'password1', 'password2', 'nom', 'prenom', 'lieu_naissance', 'telephone', 'date_naissance']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['prenom']
        user.last_name = self.cleaned_data['nom']

        if commit:
            user.save()
            # Créez un profil Citoyen après avoir sauvegardé l'utilisateur
            Citoyen.objects.create(
                user=user,
                lieu_naissance=self.cleaned_data['lieu_naissance'],
                telephone=self.cleaned_data['telephone'],
                date_naissance=self.cleaned_data['date_naissance']
            )

        return user



class AuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nom d\'utilisateur',
        }),
        label='Nom d\'utilisateur'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mot de passe',
        }),
        label='Mot de passe'
    )


class ActeNaissanceForm(forms.Form):
    nom_enfant = forms.CharField(label="Nom de l'enfant", max_length=100, required=True)
    prenom_enfant = forms.CharField(label="Prénom de l'enfant", max_length=100, required=True)
    date_naissance = forms.DateField(label="Date de naissance", widget=forms.SelectDateWidget(years=range(1900, 2024)), required=True)
    lieu_naissance = forms.CharField(label="Lieu de naissance", max_length=100, required=True)
    nom_pere = forms.CharField(label="Nom du père", max_length=100, required=True)
    prenom_pere = forms.CharField(label="Prénom du père", max_length=100, required=True)
    nom_mere = forms.CharField(label="Nom de la mère", max_length=100, required=True)
    prenom_mere = forms.CharField(label="Prénom de la mère", max_length=100, required=True)


class ActeMariageForm(forms.Form):
    nom_epoux = forms.CharField(label="Nom de l'époux", max_length=100, required=True)
    prenom_epoux = forms.CharField(label="Prénom de l'époux", max_length=100, required=True)
    nom_epouse = forms.CharField(label="Nom de l'épouse", max_length=100, required=True)
    prenom_epouse = forms.CharField(label="Prénom de l'épouse", max_length=100, required=True)
    nom_mariage = forms.CharField(label="Nom de mariage", max_length=100, required=True)


