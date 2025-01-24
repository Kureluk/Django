from django.http import HttpResponse
from django.shortcuts import redirect, render

from users.forms import CreateUser, EditUser
from users.models import Users



def home(request):
    users = Users.objects.all()
    return render(request, "index.html", {"users": users})


def create(request):
    form = CreateUser()

    if request.method == "POST":
        form = CreateUser(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/users/home")
        else:
            print(form.errors)  

    return render(request, "create.html", {"form": form})



def edit(request, id):
    try:
        user = Users.objects.get(id=id)
    except Users.DoesNotExist:
        return redirect("/users/home")

    form = EditUser(instance=user)

    if request.method == "POST":
        form = EditUser(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect("/users/home")

    return render(request, "edit.html", {"form": form})


def details(request, id):
    user = Users.objects.get(id=id)

    return render(request, "details.html", {"user": user})


def delete(request, id):
    user = Users.objects.get(id=id)

    if user is not None:
        user.delete()

    return redirect("/users/home")

