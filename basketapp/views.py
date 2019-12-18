from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from mainapp.models import Product
from .models import BasketSlot


def add(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    basket_slot = BasketSlot.objects.filter(product=product_pk).first()
    if basket_slot:
        basket_slot.quantity += 1
        basket_slot.save()
    else:
        BasketSlot(user=request.user, product=product).save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove(request, product_pk=None):
    product = get_object_or_404(Product, pk=product_pk)
    basket_slot = BasketSlot.objects.filter(user=request.user, product=product).first()

    if basket_slot:
        if basket_slot.quantity <= 1:
            basket_slot.delete()
        else:
            basket_slot.quantity -= 1
            basket_slot.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))