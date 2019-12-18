import json, os
from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory



# Create your views here.
#def loadMenuFromJSON():
#    with open(os.path.join('mainapp', 'json', 'menu.json'), 'r') as infile:
#        return json.load(infile)

def main(request):
    return render(request, 'mainapp/main.html', context={'title': 'Главная'})


def products(request, pk=None):
    products = Product.objects.all()
    if pk:
        products = products.filter(category=pk)

    context = {'products': products,
               'categories' : ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)


#def categories(request):
    #links_menu = loadMenuFromJSON()
#    context = {'links_menu': links_menu, 'categories': ProductCategory.objects.all()}
 #   return render(request, 'mainapp/products.html', context)


def contacts(request):
    return render(request, "mainapp/contacts.html", context={'title': 'Контакты'})





