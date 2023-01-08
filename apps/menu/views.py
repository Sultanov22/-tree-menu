from django.shortcuts import render
from apps.settings.models import Setting
from apps.menu.models import Menus


# Create your views here.

def menus(request, id):
    home = Setting.objects.latest('id')
    menu = Menus.objects.get(id = id)
    context = {
        'home' : home,
        'menu' : menu,
    }
    return render(request, 'menu.html', context)



