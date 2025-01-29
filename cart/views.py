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