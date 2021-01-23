from django import forms
from django.shortcuts import get_object_or_404

from rsc_mgmt.models import Resource, ResourceType


class CreateResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ('libele', 'capacite', 'resource_type')

    libele = forms.CharField(max_length=50)


class CreateResourceTypeForm(forms.ModelForm):
    class Meta:
        model = ResourceType
        fields = ('name',)

    name = forms.CharField(max_length=50, required=True)
