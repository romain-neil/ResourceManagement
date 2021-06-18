from django.contrib import admin
from .models import Resource, ResourceType, User

# Register your models here.
admin.site.register(Resource)
admin.site.register(ResourceType)
admin.site.register(User)
