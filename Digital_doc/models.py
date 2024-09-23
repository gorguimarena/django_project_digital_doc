from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Citoyen(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lieu_naissance = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    date_naissance = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.lieu_naissance}"


# class Demande(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     date_demand = models.DateField()
#     status = models.BooleanField()
#     type = models.CharField(max_length=100)


# class Document(models.Model):
#     demande = models.ForeignKey(Demande, on_delete=models.CASCADE)
#     content = models.TextField()
#     date_document = models.DateField()
#
#
# class Act_naissance(Document):
#     nom_enfant = models.CharField(max_length=100)
#     prenom= models.CharField(max_length=100)
#     date_naissance = models.DateField()
#     lieu_naissance = models.CharField(max_length=100)
#     nom_pere = models.CharField(max_length=100)
#     prenom_pere = models.CharField(max_length=100)
#     nom_mere = models.CharField(max_length=100)
#     prenom_mere = models.CharField(max_length=100)
#
#
# class Act_mariage(Document):
#     nom_epoux = models.CharField(max_length=100)
#     prenom_epoux = models.CharField(max_length=100)
#     nom_epouse = models.CharField(max_length=100)
#     prenom_epouse = models.CharField(max_length=100)
#     nom_marriage = models.CharField(max_length=100)


class DocumentDemande(models.Model):

    STATUS_CHOICES = [
        ('en_attente', 'En attente'),
        ('acceptee', 'Acceptée'),
        ('refusee', 'Refusée'),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='en_attente')
    document_type = models.CharField(max_length=20, null=False, blank=False)
    nom_enfant = models.CharField(max_length=100, blank=True, null=True)
    prenom_enfant = models.CharField(max_length=100, blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)
    lieu_naissance = models.CharField(max_length=100, blank=True, null=True)
    nom_pere = models.CharField(max_length=100, blank=True, null=True)
    prenom_pere = models.CharField(max_length=100, blank=True, null=True)
    nom_mere = models.CharField(max_length=100, blank=True, null=True)
    prenom_mere = models.CharField(max_length=100, blank=True, null=True)

    nom_epoux = models.CharField(max_length=100, blank=True, null=True)
    prenom_epoux = models.CharField(max_length=100, blank=True, null=True)
    nom_epouse = models.CharField(max_length=100, blank=True, null=True)
    prenom_epouse = models.CharField(max_length=100, blank=True, null=True)
    nom_mariage = models.CharField(max_length=100, blank=True, null=True)

    date_demande = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return f"Demande de {self.document_type} le {self.date_demande}"


class Mairie(models.Model):
    nom_maire = models.CharField(max_length=100)
    departement = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)


class Agent(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    citoyen = models.OneToOneField(Citoyen, on_delete=models.CASCADE,null=True)
    mairie = models.CharField(max_length=50,null=False,blank=True)
    post = models.CharField(max_length=100)

    def __str__(self):
        return f"Agent: Citoyen: {self.citoyen.user.username}, Mairie: {self.mairie}"


class Role(AbstractUser):
    ROLE_CHOICES = [
        ('citoyen', 'Citoyen'),
        ('agent', 'Agent'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='citoyen')