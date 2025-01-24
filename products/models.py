from django.db import models



class Product(models.Model):
    CATEGORY_CHOICES = [
        (0, 'Food'),
        (1, 'Not food'),
    ]

    name = models.CharField(max_length=255)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=0)
    photo = models.ImageField(upload_to="media/", blank=True)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=255, choices = Product.CATEGORY_CHOICES,default = 0) 

    def __str__(self):
        return self.name
