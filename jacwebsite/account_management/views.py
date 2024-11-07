from django.shortcuts import render, redirect
from django.views.decorators.csrf import requires_csrf_token
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import User, Parent, Eleve, MembreDirecction

# Create your views here.
@requires_csrf_token
def connectionpage(request):
    return render(request,"account_management/index.html")


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            identifiant = form.cleaned_data['identifiant']
            password = form.cleaned_data['password']

            user = form.save(commit=False)
            user.adresse_email = email
            user.set_password(password)

            if identifiant:
                # Récupérer les informations de l'utilisateur existant
                if Parent.objects.filter(id=identifiant).exists():
                    parent = Parent.objects.get(id=identifiant)
                    user.type_compte = 'P'  # Parent
                    # Remplir d'autres informations si nécessaire
                elif Eleve.objects.filter(id=identifiant).exists():
                    eleve = Eleve.objects.get(id=identifiant)
                    user.type_compte = 'E'  # Élève
                    # Remplir d'autres informations si nécessaire
                elif MembreDirecction.objects.filter(id=identifiant).exists():
                    membre = MembreDirecction.objects.get(id=identifiant)
                    user.type_compte = 'D'  # Direction
                    # Remplir d'autres informations si nécessaire
            else:
                # Si aucun identifiant n'est fourni, utilisez des valeurs par défaut
                user.type_compte = 'S'  # Standard

            user.save()
            messages.success(request, "Inscription réussie ! Un email avec votre identifiant a été envoyé.")
            # Envoyer un email avec l'identifiant ici

            return redirect('login')  # Rediriger vers la page de connexion
    else:
        form = UserRegistrationForm()

    return render(request, "account_management/index.html", {'form': form})
