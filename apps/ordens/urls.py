from django.urls import path

from . import views

urlpatterns = [

    path(
        "",
        views.lista_ordens,
        name="lista_ordens",
    ),

    path(
        "novo/",
        views.nova_ordem,
        name="nova_ordem",
    ),

    path(
        "<int:pk>/editar/",
        views.editar_ordem,
        name="editar_ordem",
    ),

    path(
        "<int:pk>/excluir/",
        views.excluir_ordem,
        name="excluir_ordem",
    ),

]