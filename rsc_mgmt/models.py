from django.db import models
from django.utils.translation import gettext_lazy as _

"""
Représente une ressource
"""


class Resource(models.Model):

    """
    Représente un type de ressource
    Pourrait être changé en une relation avec un autre object
    pour avoir plusieurs type d'objets
    """

    class ResourceType(models.TextChoices):
        CAR = 'CAR', _('Voiture')
        ROOM = 'ROO', _('Salle')
        COMPUTER = 'CMP', _('Computer')

    resource_typpe = models.CharField(
        max_length=3,
        choices=ResourceType.choices,
        default=ResourceType.CAR,
    )
