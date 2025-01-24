from django.urls import path

from cart import views

urlpatterns = [
    path("f", views.index),
    path("add/<int:id>", views.add),
    path("deleteCart/<int:id>", views.delete),
]
