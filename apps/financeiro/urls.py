from django.urls import path

from . import views

urlpatterns = [

    path(
        "",
        views.lista_movimentacoes,
        name="lista_movimentacoes",
    ),

    path(
        "novo/",
        views.nova_movimentacao,
        name="nova_movimentacao",
    ),

    path(
        "<int:pk>/editar/",
        views.editar_movimentacao,
        name="editar_movimentacao",
    ),

    path(
        "<int:pk>/excluir/",
        views.excluir_movimentacao,
        name="excluir_movimentacao",
    ),

]