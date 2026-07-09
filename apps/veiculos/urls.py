from django.urls import path

from . import views


urlpatterns = [

    path(
        "",
        views.lista_veiculos,
        name="lista_veiculos",
    ),

    path(
        "novo/",
        views.novo_veiculo,
        name="novo_veiculo",
    ),

    path(
        "<int:pk>/editar/",
        views.editar_veiculo,
        name="editar_veiculo",
    ),

    path(
        "<int:pk>/excluir/",
        views.excluir_veiculo,
        name="excluir_veiculo",
    ),
    path(
    "<int:pk>/excluir/",
    views.excluir_veiculo,
    name="excluir_veiculo",
),

]