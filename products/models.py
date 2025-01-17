from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    clas = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="media/", blank=True)

    def __str__(self):
        return self.name
