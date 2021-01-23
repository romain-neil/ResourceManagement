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
    capacite = models.IntegerField()

    def __str__(self):
        return self.libele
