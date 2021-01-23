from django import forms

from rsc_mgmt.models import Resource, ResourceType, User


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


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    username = forms.CharField(max_length=50, required=True)
    password = forms.PasswordInput()


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    username = forms.CharField(max_length=50, required=True)
    password = forms.PasswordInput()
