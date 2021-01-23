from django.db import models
from django.utils.translation import gettext_lazy as _


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
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.resource_type


class User(models.Model):
    """
    Classe qui rerésente un utilisateur

    Amélioration possibles: activation du compte via l'administration (ajout d'un champ is_activated)
    """
    username = models.CharField(max_length=50),
    password = models.CharField(max_length=50),
    admin = models.BooleanField(default=False)

    def is_admin(self):
        return self.admin

    def __str__(self):
        return self.username
