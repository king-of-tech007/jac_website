from django import forms
from .models import User, Parent, Eleve, MembreDirecction

class UserRegistrationForm(forms.ModelForm):
    identifiant = forms.CharField(max_length=18, required=False, label='Identifiant')
    email = forms.EmailField(required=True, label='Email')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='Password')

    class Meta:
        model = User
        fields = ['email', 'identifiant', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(adresse_email=email).exists():
            raise forms.ValidationError("Cet email est déjà lié à un compte.")
        return email

    def clean_identifiant(self):
        identifiant = self.cleaned_data.get('identifiant')
        if identifiant:
            # Vérifiez si l'identifiant existe dans les autres modèles
            if (Parent.objects.filter(id=identifiant).exists() or
                Eleve.objects.filter(id=identifiant).exists() or
                MembreDirecction.objects.filter(id=identifiant).exists()):
                return identifiant
            else:
                raise forms.ValidationError("L'identifiant n'existe pas dans les comptes autorisés.")
        return None