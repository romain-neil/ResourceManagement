from django.http import HttpResponse
from django.shortcuts import render,redirect

from rsc_mgmt.models import Resource, ResourceType
from .forms import CreateResourceTypeForm, CreateResourceForm


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
    if request.method == 'POST':
        form = CreateResourceForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')
    else:
        form = CreateResourceForm()

    return render(request, 'rsc_mgmt/create_resource.html', locals())


def delete_res(request):
    return HttpResponse("bla bla bla")


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


def delete_res_type(request):
    return HttpResponse("Self explained")


def login(request):
    return HttpResponse("login page")


def register(request):
    return HttpResponse("register page")
