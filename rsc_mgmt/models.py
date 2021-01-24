from django.db import models


class ResourceType(models.Model):
    """
    Représente un type de ressource
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Resource(models.Model):
    """
    Représente une ressource
    """

    resource_type = models.ForeignKey(ResourceType, on_delete=models.CASCADE)
    libele = models.CharField(max_length=50, default="")
    place = models.CharField(max_length=50, default="")  # Localisation de la ressource
    capacite = models.IntegerField()

    def __str__(self):
        return self.libele


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    admin = models.BooleanField(default=False)

    def is_admin(self):
        return self.admin
