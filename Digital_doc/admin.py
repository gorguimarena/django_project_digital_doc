from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Citoyen, Mairie, Agent, DocumentDemande, Role


# Définir un modèle Inline pour Citoyen
class CitoyenInline(admin.StackedInline):
    model = Citoyen
    can_delete = False
    verbose_name_plural = 'Profils Citoyens'


# Étendre le modèle UserAdmin pour inclure les informations du Citoyen
class UserAdmin(BaseUserAdmin):
    inlines = (CitoyenInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_telephone')

    def get_telephone(self, instance):
        # Accès au profil Citoyen pour obtenir le téléphone
        return instance.citoyen.telephone if hasattr(instance, 'citoyen') else 'N/A'

    get_telephone.short_description = 'Téléphone'


admin.site.register(User, UserAdmin)
admin.site.register(Role)
admin.site.register(Citoyen)
admin.site.register(Mairie)
admin.site.register(Agent)
admin.site.register(DocumentDemande)
