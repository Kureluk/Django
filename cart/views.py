from django.shortcuts import redirect, render
from cart.cart import addProduct, getProduct
from products.models import Product


def cart(request):
    items = getProduct(request.session)         
    products = Product.objects.filter(id__in=items.keys())
    return render(request, "cart/index.html", {"products": products})

def add(request, id):
    if Product.objects.get(id=id) is None:
        return redirect("/cart")    

    addProduct(request.session, id)
    return redirect("/cart")

from cart.cart import add_to_cart, get_cart, remove_from_cart
from products.models import Product

def index(request):

    items = get_cart(request.session)

    products = Product.objects.filter(id__in=items.keys())
    
    return render(request, "f.html", {"products": products})



def add(request, id, quantity = 1):

    if Product.objects.get(id=id) is None:

        return redirect("/products")
    
    add_to_cart(request.session, id, quantity)

    return redirect("/products")


def delete(request, id):

    if Product.objects.get(id=id) is None:

        return redirect("/cart/f")
    
    remove_from_cart(request.session, id)

    return redirect("/cart/f")

