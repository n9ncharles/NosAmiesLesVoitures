from django.contrib.auth import get_user_model, login, authenticate, logout
from django.shortcuts import render, redirect

User = get_user_model()


# Create your views here.
def inscription(request):
    if request.method == "POST":
        nom = request.POST.get("lastname")
        prenom = request.POST.get("firstname")
        nom_utilisateur = request.POST.get("username")
        mot_de_pase = request.POST.get("password")

        users = User.objects.create_user(last_name=nom,
                                            first_name=prenom,
                                            username=nom_utilisateur,
                                            password=mot_de_pase)

        login(request, users)
        return redirect('index')
    return render(request, 'inscription.html')


def connexion(request):
    if request.method == "POST":
        nom_utilisateur = request.POST.get("username")
        mot_de_pase = request.POST.get("password")

        users = authenticate(username=nom_utilisateur,
                                password=mot_de_pase)

        if users:
            login(request, users)
            return redirect('index')

    return render(request, 'connexion.html')


def deconnexion(request):
    logout(request)
    return redirect('index')