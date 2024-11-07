import random


from django.db import models
import hashlib
from django.contrib.auth.hashers import make_password, check_password


# Create your models here.
def generate_id(nom, prenom, date_naissance, genre):
    """Génère un identifiant unique de 16 caractères."""
    input_str = f"{nom}{prenom}{date_naissance}{genre}"
    hashed = int(hashlib.sha256(input_str.encode()).hexdigest(), 16)
    return str(hashed % 10**16).zfill(16)

def generate_id_user(nom, prenom, date_naissance, genre):
    """Génère un identifiant unique de 16 caractères."""
    input_str = f"{nom}{prenom}{date_naissance}{genre}{random.randint(111111111111111111,999999999999999999)}"
    hashed = int(hashlib.sha256(input_str.encode()).hexdigest(), 16)
    return str(hashed % 10**18).zfill(18)


class User(models.Model):
    GENRE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]
    COMPTES_CHOICES = [
        ('S', 'Standar'),
        ('E', 'Eleve'),
        ('P', 'Parent'),
        ('D', 'Direction Members'),

    ]

    id = models.CharField(max_length=18, primary_key=True, editable=False)
    nom = models.CharField(max_length=25, null=True)
    prenom = models.CharField(max_length=50, null=True)
    nom_affichage = models.CharField(max_length=100, unique=True, null=True)
    age = models.PositiveIntegerField(null=True)
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES, null=True)
    date_naissance = models.DateField(null=True)
    nationalite = models.CharField(max_length=100, null=True)
    numero_telephone = models.CharField(max_length=15, null=True)
    adresse_email = models.EmailField(unique=True, null=False)
    profil = models.ImageField(upload_to='profil_images/', null=True, blank=True)
    password = models.CharField(max_length=256, null=False)
    date_inscription = models.DateField(auto_now_add=True)
    numero_rue = models.CharField(max_length=50, null=True)
    nom_rue = models.CharField(max_length=100, null=True)
    ville = models.CharField(max_length=100, null=True)
    code_postal = models.CharField(max_length=20, null=True)
    type_compte = models.CharField(max_length=1, choices=COMPTES_CHOICES, null=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = generate_id(self.nom, self.prenom, self.date_naissance.strftime('%Y-%m-%d'), self.genre)
        if self.password and not self.password.startswith(
                'pbkdf2_sha256$'):  # Vérifiez si le mot de passe est déjà haché
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.nom_affichage})"

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


class Eleve(models.Model):
    GENRE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]

    id = models.CharField(max_length=16, primary_key=True, editable=False)
    nom = models.CharField(max_length=25, null=False)
    prenom = models.CharField(max_length=50, null=False)
    nom_affichage = models.CharField(max_length=100, unique=True, null=False)
    age = models.PositiveIntegerField(null=False)
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES, null=False)
    date_naissance = models.DateField(null=False)
    nationalite = models.CharField(max_length=100, null=False)
    numero_telephone = models.CharField(max_length=15, null=False)
    adresse_email = models.EmailField(unique=True, null=False)
    profil = models.ImageField(upload_to='profil_images/', null=True, blank=True)
    password = models.CharField(max_length=256, null=False)
    date_inscription = models.DateField(auto_now_add=True)
    numero_rue = models.CharField(max_length=50, null=False)
    nom_rue = models.CharField(max_length=100, null=False)
    ville = models.CharField(max_length=100, null=False)
    code_postal = models.CharField(max_length=20, null=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = generate_id_user(self.nom, self.prenom, self.date_naissance.strftime('%Y-%m-%d'), self.genre)
        if self.password and not self.password.startswith(
                'pbkdf2_sha256$'):  # Vérifiez si le mot de passe est déjà haché
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.nom_affichage})"

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


class Parent(models.Model):
    GENRE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]

    id = models.CharField(max_length=16, primary_key=True, editable=False)
    nom = models.CharField(max_length=25, null=False)
    prenom = models.CharField(max_length=50, null=False)
    nom_affichage = models.CharField(max_length=100, unique=True, null=False)
    age = models.PositiveIntegerField(null=False)
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES, null=False)
    date_naissance = models.DateField(null=False)
    nationalite = models.CharField(max_length=100, null=False)
    numero_telephone = models.CharField(max_length=15, null=False)
    adresse_email = models.EmailField(unique=True, null=False)
    profil = models.ImageField(upload_to='profil_images/', null=True, blank=True)
    password = models.CharField(max_length=256, null=False)
    date_inscription = models.DateField(auto_now_add=True)
    numero_rue = models.CharField(max_length=50, null=False)
    nom_rue = models.CharField(max_length=100, null=False)
    ville = models.CharField(max_length=100, null=False)
    code_postal = models.CharField(max_length=20, null=False)
    enfants = models.ManyToManyField(Eleve, related_name='parents_eleve', blank=True)
    est_enfant = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = generate_id(self.nom, self.prenom, self.date_naissance.strftime('%Y-%m-%d'), self.genre)
        if self.password and not self.password.startswith(
                'pbkdf2_sha256$'):  # Vérifiez si le mot de passe est déjà haché
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.nom_affichage})"

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


class MembreDirecction(models.Model):
    GENRE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]

    TACHE_CHOICES = [
        ('secretaire', 'Secrétaire', 2),
        ('economiste', 'Économiste', 3),
        ('prefet', 'Préfet', 4),
        ('directeur', 'Directeur', 5),
        ('informaticien', 'Informaticien', 2),
        ('professeur', 'professeur', 1),
    ]

    id = models.CharField(max_length=16, primary_key=True, editable=False)
    nom = models.CharField(max_length=25, null=False)
    prenom = models.CharField(max_length=50, null=False)
    nom_affichage = models.CharField(max_length=100, unique=True, null=False)
    age = models.PositiveIntegerField(null=False)
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES, null=False)
    date_naissance = models.DateField(null=False)
    nationalite = models.CharField(max_length=100, null=False)
    numero_telephone = models.CharField(max_length=15, null=False)
    adresse_email = models.EmailField(unique=True, null=False)
    profil = models.ImageField(upload_to='profil_images/', null=True, blank=True)
    password = models.CharField(max_length=256, null=False)
    date_inscription = models.DateField(auto_now_add=True)
    numero_rue = models.CharField(max_length=50, null=False)
    nom_rue = models.CharField(max_length=100, null=False)
    ville = models.CharField(max_length=100, null=False)
    code_postal = models.CharField(max_length=20, null=False)
    tache = models.CharField(max_length=50, choices=[(task[0], task[1]) for task in TACHE_CHOICES], null=False)
    niveau_accreditation = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = generate_id(self.nom, self.prenom, self.date_naissance.strftime('%Y-%m-%d'), self.genre)
        if self.password and not self.password.startswith(
                'pbkdf2_sha256$'):  # Vérifiez si le mot de passe est déjà haché
            self.set_password(self.password)
        super().save(*args, **kwargs)

        # Définir le niveau d'accréditation en fonction de la tâche
        for task in self.TACHE_CHOICES:
            if task[0] == self.tache:
                self.niveau_accreditation = task[2]
                break

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.nom_affichage})"

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

