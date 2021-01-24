from django.contrib import admin
from .models import Resource, ResourceType, User

# Register your models here.
admin.register(Resource)
admin.register(ResourceType)
admin.register(User)
