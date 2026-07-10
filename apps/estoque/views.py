from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import Produto
from .forms import ProdutoForm

def lista_produtos(request):

    produtos = Produto.objects.all()

    context = {
        "produtos": produtos,
    }

    return render(
        request,
        "estoque/lista.html",
        context
    )
def novo_produto(request):

    if request.method == "POST":

        form = ProdutoForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("lista_produtos")

    else:

        form = ProdutoForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "estoque/formulario.html",
        context,
    )
def editar_produto(request, pk):

    produto = get_object_or_404(
        Produto,
        pk=pk
    )

    if request.method == "POST":

        form = ProdutoForm(
            request.POST,
            instance=produto
        )

        if form.is_valid():

            form.save()

            return redirect("lista_produtos")

    else:

        form = ProdutoForm(instance=produto)

    context = {
        "form": form,
    }

    return render(
        request,
        "estoque/formulario.html",
        context,
    )
def excluir_produto(request, pk):

    produto = get_object_or_404(
        Produto,
        pk=pk
    )

    if request.method == "POST":

        produto.delete()

        return redirect("lista_produtos")

    context = {
        "produto": produto,
    }

    return render(
        request,
        "estoque/excluir.html",
        context,
    )
