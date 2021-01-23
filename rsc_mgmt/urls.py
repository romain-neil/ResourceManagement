from django.conf.urls import url
from django.urls import include, path

from . import views

"""
Routes pour les ressources (detail, suppressions, edition, ...)
"""
rsc_patterns = [
    url('create/', views.create_res, name="create_res"),
    path('detail/<int:rid>', views.detail, name="resource_detail"),
    path('delete/<int:rid>', views.delete, name="resource_delete"),
    path('edit/<int:rid>', views.edit),
]

"""
Routes pour les types de ressources (création et suppression)
"""
rsc_type_patterns = [
    path('create/', views.create_res_type, name="create_res_type"),
    path('delete/<int:rid>', views.delete_res_type, name="delete_resource_type"),
]

urlpatterns = [
    path('resource/', include(rsc_patterns)),
    path('resource_type/', include(rsc_type_patterns)),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('', views.index, name='index')
]
