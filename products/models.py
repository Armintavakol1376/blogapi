from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=13)

    def __str__(self):
        return self.name
