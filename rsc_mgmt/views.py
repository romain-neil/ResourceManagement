from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import *


def is_login(request):
    return request.session.__contains__('user')


# Pourrais être amélioré en utilisant les actions (ex: 'can_create_resource', 'can_view', ...)
def is_admin(user):
    return user['is_admin']


# Create your views here.
def index(request):
    if not is_login(request):
        return redirect('login')

    order = request.GET.get('order', default='libele')
    res = Resource.objects.order_by(order)

    """
    Si on a un signe négatif dans le paramètre de trie, on retire ce signe pour inverser le filtre
    """
    if "-" in order:  # Si il y a un paramètre
        order = ''  # Alors on retire le signe négatif
    else:
        order = "-"

    return render(request, 'rsc_mgmt/index.html', {
        'res': res,
        'order_sign': order,
        'type': ResourceType.objects.all(),
        'user': request.session['user']
    })


def detail(request, rid=0):
    try:
        r = Resource.objects.get(pk=rid)

        return JsonResponse({
            'libele': r.libele,
            'capacite': r.capacite,
            'type': r.resource_type.__str__(),
            'loc': r.place
        })
    except Resource.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'resource not found'
        })


# Suppression de ressource
def delete(request, rid=0):
    if not is_admin(request.session['user']):
        return redirect('index')

    try:
        Resource(pk=rid).delete()
    except Resource.DoesNotExist:
        err_msg = "La resource n'a pa été trouvée"

    return redirect('index')


def edit(request, rid=None):
    res = None

    if rid is not None:
        res = Resource.objects.get(pk=rid)

    form = CreateResourceForm(request.POST or None, instance=res)
    if request.POST and form.is_valid():
        form.save()

        return redirect('index')

    return render(request, 'rsc_mgmt/create_resource.html', {
        'form': form
    })


def create_res(request):
    # Formulaire de création de ressource
    if not is_admin(request.session['user']):
        return redirect('index')

    if request.method == 'POST':
        form = CreateResourceForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')
    else:
        form = CreateResourceForm()

    return render(request, 'rsc_mgmt/create_resource.html', locals())


def create_res_type(request):
    if not is_admin(request.session['user']):
        return redirect('index')

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
    if not is_admin(request.session.get('user')):
        return redirect('index')

    try:
        ResourceType(pk=rid).delete()
    except ResourceType.DoesNotExist:
        err_msg = "La resource n'a pa été trouvée"

        messages.add_message(request, messages.ERROR, err_msg)

    return redirect('index')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            mdp = form.cleaned_data['password']

            try:
                user = User.objects.get(username=username, password=mdp)
                u = {
                    'username': user.username,
                    'is_admin': user.is_admin()
                }

                request.session['user'] = u

                return redirect('index')
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
