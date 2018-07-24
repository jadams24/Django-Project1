''' personal URL configuration '''

from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^contact/', views.contact, name='contact')
]
