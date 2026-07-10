from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import Movimentacao
from .forms import MovimentacaoForm


def lista_movimentacoes(request):

    movimentacoes = Movimentacao.objects.all()

    context = {
        "movimentacoes": movimentacoes,
    }

    return render(
        request,
        "financeiro/lista.html",
        context,
    )


def nova_movimentacao(request):

    if request.method == "POST":

        form = MovimentacaoForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("lista_movimentacoes")

    else:

        form = MovimentacaoForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "financeiro/formulario.html",
        context,
    )


def editar_movimentacao(request, pk):

    movimentacao = get_object_or_404(
        Movimentacao,
        pk=pk,
    )

    if request.method == "POST":

        form = MovimentacaoForm(
            request.POST,
            instance=movimentacao,
        )

        if form.is_valid():

            form.save()

            return redirect("lista_movimentacoes")

    else:

        form = MovimentacaoForm(
            instance=movimentacao,
        )

    context = {
        "form": form,
    }

    return render(
        request,
        "financeiro/formulario.html",
        context,
    )


def excluir_movimentacao(request, pk):

    movimentacao = get_object_or_404(
        Movimentacao,
        pk=pk,
    )

    if request.method == "POST":

        movimentacao.delete()

        return redirect("lista_movimentacoes")

    context = {
        "movimentacao": movimentacao,
    }

    return render(
        request,
        "financeiro/excluir.html",
        context,
    )