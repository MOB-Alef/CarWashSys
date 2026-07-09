from django.shortcuts import render, redirect, get_object_or_404

from .models import Veiculo
from .forms import VeiculoForm


def lista_veiculos(request):

    veiculos = Veiculo.objects.all()

    context = {
        "veiculos": veiculos,
    }

    return render(
        request,
        "veiculos/lista.html",
        context,
    )


def novo_veiculo(request):

    if request.method == "POST":

        form = VeiculoForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("lista_veiculos")

    else:

        form = VeiculoForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "veiculos/formulario.html",
        context,
    )


def editar_veiculo(request, pk):

    veiculo = get_object_or_404(
        Veiculo,
        pk=pk,
    )

    if request.method == "POST":

        form = VeiculoForm(
            request.POST,
            instance=veiculo,
        )

        if form.is_valid():

            form.save()

            return redirect("lista_veiculos")

    else:

        form = VeiculoForm(
            instance=veiculo,
        )

    context = {
        "form": form,
    }

    return render(
        request,
        "veiculos/formulario.html",
        context,
    )


def excluir_veiculo(request, pk):

    veiculo = get_object_or_404(
        Veiculo,
        pk=pk,
    )

    if request.method == "POST":

        veiculo.delete()

        return redirect("lista_veiculos")

    context = {
        "veiculo": veiculo,
    }

    return render(
        request,
        "veiculos/excluir.html",
        context,
    )
def excluir_veiculo(request, pk):

    veiculo = get_object_or_404(
        Veiculo,
        pk=pk
    )

    if request.method == "POST":

        veiculo.delete()

        return redirect("lista_veiculos")

    context = {
        "veiculo": veiculo,
    }

    return render(
        request,
        "veiculos/excluir.html",
        context,
    )    