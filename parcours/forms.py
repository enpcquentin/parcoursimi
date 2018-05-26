from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from parcours.models import UserProfile, Master


class ConnexionForm(forms.Form):
    """ Formulaire de connexion """
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    """ Formulaire d'utilisateur """
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    def clean(self):
        cleaned_data = self.cleaned_data
        mail = self.cleaned_data.get('email')
        if mail=="": # Est-ce que l'utilisateur a bien spécifié une adresse mail ?
            raise forms.ValidationError("Merci de spécifier une adresse mail")
        return cleaned_data


class UserProfileForm(forms.ModelForm):
    """ Formulaire de profil """
    class Meta:
        model = UserProfile
        fields = ('master', 'option')
        
        
class MasterForm(forms.ModelForm):
    """ Formulaire de profil """
    class Meta:
        model = Master
        labels = {
        "website": "Site web du master",
        "troisa_possible": "Cocher si les étudiants peuvent choisir ce master comme 3A"
        }
        fields = ('name', 'website', 'troisa_possible')