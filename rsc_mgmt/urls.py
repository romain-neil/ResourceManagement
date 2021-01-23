from django.conf.urls import url
from django.urls import include, path

from . import views

"""
Routage pour les ressources (detail, suppressions, edition, ...)
"""
rsc_patterns = [
    url('create/', views.create_res, name="create_res"),
    path('detail/<int:id>', views.detail),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
]

rsc_type_patterns = [
    url('create/', views.create_res_type, name="create_res_type"),
    path('delete/', views.delete_res_type),
]

urlpatterns = [
    path('resource/', include(rsc_patterns)),
    path('resource_type/', include(rsc_type_patterns)),
    path('login/', views.login),
    path('', views.index, name='index')
]