from django.urls import path

from products import views

urlpatterns = [
    path("", views.list),
    path("createProduct/", views.create),
    path("editProduct/<int:id>", views.edit),
    path("detailsProduct/<int:id>", views.details),
    path("delete/<int:id>", views.delete),
]
