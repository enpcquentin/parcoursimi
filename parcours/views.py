from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from parcours.forms import UserProfileForm, UserForm


def home(request):
        return render(request, 'parcours/home.html')

        
def connexion(request):
    """Vue de connexion. Si les informations renseignées sont correctes, connecte l'utilisateur
    et le redirige vers la page d'accueil"""

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            # on vérifie que le compte courant est valide et actif
            # si c'est le cas, on connecte l'utilisateur
            if user.is_active and not(user.is_superuser):
                login(request, user)
                return HttpResponseRedirect('/parcours/home')
            else:
                return HttpResponse("Vous n'êtes autorisé à vous connecter.")
        else:
            print("Erreur dans le mot de passe ou l'identifiant : {0}, {1}".format(username, password))
            return HttpResponse("Erreur dans le mot de passe ou l'identifiant.")
    else:
        return render(request, 'parcours/connexion.html', {'erreur' : False})


def inscription(request):
    """Vue d'inscription qui enregistre l'entrée utilisateur, l'entrée profil et les relie entre eux"""

    # un booléan pour tester la validation de l'enregistrement
    registered = False
    # on a besoin d'une méthode POST pour le formulaire
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
                # on signale au template que l'enregistrement s'est correctement réalisé
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
                  'parcours/inscription.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered,'adresse_incorrecte': False})




def deconnexion(request):
    """ Vue de déconnexion """

    logout(request)
    return render(request, 'parcours/home.html')



