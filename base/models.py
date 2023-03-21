from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
    ordered_date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=6, decimal_places=2)
