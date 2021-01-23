from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from .forms import *


def is_login(request):
    return request.session.__contains__('user')


# Create your views here.
def index(request):
    if not is_login(request):
        return redirect('login')

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
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            mdp = form.cleaned_data['password']

            try:
                user = User.objects.get(username=username, password=mdp)
                request.session['user'] = user
            except User.DoesNotExist:
                return redirect('login')

    else:
        form = LoginForm()

    return render(request, 'rsc_mgmt/login.html', locals())


def logout(request):
    if is_login(request):
        del request.session['user']

    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            mdp = form.cleaned_data['password']

            User(username=username, password=mdp).save()

            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'rsc_mgmt/register.html', locals())
