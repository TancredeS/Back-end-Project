from django.urls import path

from . import views

# This is the URL for the index page.

urlpatterns = [
    path('<int:userid>', views.index, name='index'),
    path('<int:userid>/addclothes', views.addclothes, name='addclothes'),
    path('<int:userid>/remove_clothes', views.remove_clothes, name='remove_clothes'),
    path('<int:userid>/edit_clothes', views.edit_clothes, name='edit_clothes'),
    path('<int:userid>/clothes_list', views.clothes_list, name='clothes_list'),
]