import json, os
from django.shortcuts import render
from mainapp.models import Product
from mainapp.models import ProductCategory



# Create your views here.
def loadMenuFromJSON():
    with open(os.path.join('mainapp', 'json', 'menu.json'), 'r') as infile:
        return json.load(infile)

def main(request):
    return render(request, 'mainapp/main.html', context={'title': 'Главная'})


def products(request):
    links_menu = loadMenuFromJSON()
    context = {'links_menu' : links_menu, 'products': Product.objects.all()}
    return render(request, 'mainapp/products.html', context)


def categories(request):
    links_menu = loadMenuFromJSON()
    context = {'links_menu': links_menu, 'categories': ProductCategory.objects.all()}
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    return render(request, "mainapp/contacts.html", context={'title': 'Контакты'})





