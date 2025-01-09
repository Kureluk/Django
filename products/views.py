from django.shortcuts import render, redirect

from products.models import Product
from products.forms import CreateProduct, EditProduct


def list(request):
    product = Product.objects.all()
    return render(request, "list.html", {"products": product})


def details(request, id):
    product = Product.objects.get(id=id)

    return render(request, "detailsProduct.html", {"product": product})


def delete(request, id):
    product = Product.objects.get(id=id)

    if product is not None:
        product.delete()

    return redirect("/products")


def create(request):
    form = CreateProduct()

    if request.method == "POST":
        form = CreateProduct(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/products")

    return render(request, "createProduct.html", {"form": form})


def edit(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return redirect("/products")

    form = EditProduct(instance=product)

    if request.method == "POST":
        form = EditProduct(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect("/products")

    return render(request, "editProduct.html", {"form": form})
