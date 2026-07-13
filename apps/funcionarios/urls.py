from django.urls import path

from . import views

urlpatterns = [

    path(
        "",
        views.lista_funcionarios,
        name="lista_funcionarios",
    ),

    path(
        "novo/",
        views.novo_funcionario,
        name="novo_funcionario",
    ),

    path(
        "<int:pk>/editar/",
        views.editar_funcionario,
        name="editar_funcionario",
    ),

    path(
        "<int:pk>/excluir/",
        views.excluir_funcionario,
        name="excluir_funcionario",
    ),

]