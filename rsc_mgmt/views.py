from django.http import HttpResponse
from django.shortcuts import render

from rsc_mgmt.models import Resource, ResourceType


# Create your views here.
def index(request):
    return render(request, 'rsc_mgmt/index.html', {'res': Resource.objects.all(), 'type': ResourceType.objects.all()})


def detail(request, rsc_id):
    return render(request, 'rsc_mgmt/detail.html')


def edit(request, rsc_id):
    return HttpResponse("Edit page, id : %i" % rsc_id)


def delete(request, rsc_id):
    return HttpResponse("Page de suppression, id : %i" % rsc_id)


def create_res(request):
    # Formulaire de création de ressource
    return HttpResponse("Resource create form")


def delete_res(request):
    return HttpResponse("bla bla bla")


def create_res_type(request):
    return HttpResponse("Resource type create form")


def delete_res_type(request):
    return HttpResponse("Self explained")


def login(request):
    return HttpResponse("login page")


def register(request):
    return HttpResponse("register page")
