from django.shortcuts import render


# Create your views here.

def main(request):
    return render(request, 'mainapp/main.html', context={'title': 'Главная'})


def products(request):
    context = {'title' : 'Продукты', 'products': ['Винни Пух', 'Потапыч', 'Белоснежка', 'Крокодил Гена']}
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    return render(request, "mainapp/contacts.html", context={'title': 'Контакты'})





