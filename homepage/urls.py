from django.urls import path
from . import views

urlpatterns = [
path("", views.homepage),
path("contacts/", views.contacts),
path("operations/", views.operations),
]
