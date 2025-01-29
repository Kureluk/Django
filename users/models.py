from django.db import models

class Users(models.Model):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  
    role = models.CharField(max_length=10,default='user')  

    def __str__(self):
        return f"{self.name}"
