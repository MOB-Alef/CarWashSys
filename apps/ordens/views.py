from django.shortcuts import render, redirect, get_object_or_404

from .models import OrdemServico
from .forms import OrdemServicoForm


def lista_ordens(request):

    ordens = OrdemServico.objects.all()

    context = {
        "ordens": ordens,
    }

    return render(
        request,
        "ordens/lista.html",
        context,
    )


def nova_ordem(request):

    if request.method == "POST":

        form = OrdemServicoForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("lista_ordens")

    else:

        form = OrdemServicoForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "ordens/formulario.html",
        context,
    )


def editar_ordem(request, pk):

    ordem = get_object_or_404(
        OrdemServico,
        pk=pk,
    )

    if request.method == "POST":

        form = OrdemServicoForm(
            request.POST,
            instance=ordem,
        )

        if form.is_valid():

            form.save()

            return redirect("lista_ordens")

    else:

        form = OrdemServicoForm(
            instance=ordem,
        )

    context = {
        "form": form,
    }

    return render(
        request,
        "ordens/formulario.html",
        context,
    )


def excluir_ordem(request, pk):

    ordem = get_object_or_404(
        OrdemServico,
        pk=pk,
    )

    if request.method == "POST":

        ordem.delete()

        return redirect("lista_ordens")

    context = {
        "ordem": ordem,
    }

    return render(
        request,
        "ordens/excluir.html",
        context,
    )