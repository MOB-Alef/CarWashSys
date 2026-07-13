from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import Funcionario
from .forms import FuncionarioForm


def lista_funcionarios(request):

    funcionarios = Funcionario.objects.all()

    context = {
        "funcionarios": funcionarios,
    }

    return render(
        request,
        "funcionarios/lista.html",
        context,
    )


def novo_funcionario(request):

    if request.method == "POST":

        form = FuncionarioForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("lista_funcionarios")

    else:

        form = FuncionarioForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "funcionarios/formulario.html",
        context,
    )


def editar_funcionario(request, pk):

    funcionario = get_object_or_404(
        Funcionario,
        pk=pk,
    )

    if request.method == "POST":

        form = FuncionarioForm(
            request.POST,
            instance=funcionario,
        )

        if form.is_valid():

            form.save()

            return redirect("lista_funcionarios")

    else:

        form = FuncionarioForm(
            instance=funcionario,
        )

    context = {
        "form": form,
    }

    return render(
        request,
        "funcionarios/formulario.html",
        context,
    )


def excluir_funcionario(request, pk):

    funcionario = get_object_or_404(
        Funcionario,
        pk=pk,
    )

    if request.method == "POST":

        funcionario.delete()

        return redirect("lista_funcionarios")

    context = {
        "funcionario": funcionario,
    }

    return render(
        request,
        "funcionarios/excluir.html",
        context,
    )