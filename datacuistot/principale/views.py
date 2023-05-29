from django.shortcuts import render

# Create your views here.
def apropos(request):
    return render(request, "apropos.html")

def connexion(request):
    return render(request,"connexion.html")

def inscription (request):
    return render(request,"inscription.html")

def button(request):
    return render(request,"findyourfood.html")

def findyourfood (request):
    import random as rd
    mon_plat = []
    while len(mon_plat) < 4:
        with open('../datacuistot/principale/files/mes_aliments.txt') as file:
            meals_list = file.readlines()
            meals_random_choice = rd.choice(meals_list)
            if meals_random_choice not in mon_plat:
                mon_plat.append(meals_random_choice)
    final1 = mon_plat[0]
    final2 = mon_plat[1]
    final3 = mon_plat[2]
    final4 = mon_plat[3]
    return render(request, "findyourfood.html", {'final1':final1, 'final2':final2, 'final3':final3, 'final4':final4})

