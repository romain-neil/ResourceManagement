from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from rsc_mgmt.models import Resource, ResourceType
from .forms import CreateResourceTypeForm, CreateResourceForm


# Create your views here.
def index(request):
    return render(request, 'rsc_mgmt/index.html', {'res': Resource.objects.all(), 'type': ResourceType.objects.all()})


def detail(request, rid=0):
    try:
        r = Resource.objects.get(pk=rid)

        return JsonResponse({
            'libele': r.libele,
            'capacite': r.capacite,
            'type': r.resource_type.__str__()
        })
    except Resource.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'resource not found'
        })


# Suppression de ressource
def delete(request, rid=0):
    try:
        rsc = Resource(pk=rid).delete()
    except Resource.DoesNotExist:
        err_msg = "La resource n'a pa été trouvée"

    return redirect('index')


def edit(request, rid=0):
    return HttpResponse("Edit page, id : %i" % rid)


def create_res(request):
    # Formulaire de création de ressource
    if request.method == 'POST':
        form = CreateResourceForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')
    else:
        form = CreateResourceForm()

    return render(request, 'rsc_mgmt/create_resource.html', locals())


def create_res_type(request):
    if request.method == 'POST':
        form = CreateResourceTypeForm(request.POST)

        if form.is_valid():
            res_name = form.cleaned_data['name']

            r = ResourceType(name=res_name).save()

            return redirect('index')

    else:
        form = CreateResourceTypeForm()

    return render(request, 'rsc_mgmt/create_resource_type.html', locals())


def delete_res_type(request, rid=0):
    try:
        rsc = ResourceType(pk=rid).delete()
    except ResourceType.DoesNotExist:
        err_msg = "La resource n'a pa été trouvée"

    return redirect('index')


def login(request):
    return HttpResponse("login page")


def register(request):
    return HttpResponse("register page")
