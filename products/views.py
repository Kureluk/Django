from django.contrib import messages
from django.forms import model_to_dict
from django.shortcuts import render, redirect


from products.models import Product
from products.forms import CreateProduct, EditProduct


def list(request):
    product = Product.objects.all()
    return render(request, "list.html", {"products": product})


def details(request, id):
    product = Product.objects.get(id=id)

    return render(request, "detailsProduct.html", {
        "product": {
            **model_to_dict(product),
            "categoryName": Product.CATEGORY_CHOICES[product.category][1],
        }, 
        "return_url": "/products"})


def delete(request, id):
    product = Product.objects.get(id=id)

    if product is not None:
        product.delete()
        messages.success(request, "User deleted successfully!")

    return redirect("/products")


def create(request):
    form = CreateProduct()

    if request.method == "POST":
        form = CreateProduct(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully!")
            return redirect("/products")
        else:
            messages.error(request, "Invalid data!")

    return render(request, "createProduct.html", {"form": form, "return_url": "/products"})


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
            messages.success(request, "User changed successfully!")
            return redirect("/products")

    return render(request, "editProduct.html", {"form": form, "return_url": "/products"})
