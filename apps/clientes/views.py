from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import Cliente
from .forms import ClienteForm


def lista_clientes(request):

    clientes = Cliente.objects.all()

    context = {
        "clientes": clientes,
    }

    return render(
        request,
        "clientes/lista.html",
        context
    )


def novo_cliente(request):

    if request.method == "POST":

        form = ClienteForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("lista_clientes")

    else:

        form = ClienteForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "clientes/formulario.html",
        context,
    )

def editar_cliente(request, pk):

    cliente = get_object_or_404(
        Cliente,
        pk=pk
    )

    if request.method == "POST":

        form = ClienteForm(
            request.POST,
            instance=cliente
        )

        if form.is_valid():

            form.save()

            return redirect("lista_clientes")

    else:

        form = ClienteForm(
            instance=cliente
        )

    context = {
        "form": form,
    }

    return render(
        request,
        "clientes/formulario.html",
        context,
    )    

def excluir_cliente(request, pk):

    cliente = get_object_or_404(
        Cliente,
        pk=pk
    )

    if request.method == "POST":

        cliente.delete()

        return redirect("lista_clientes")

    context = {
        "cliente": cliente,
    }

    return render(
        request,
        "clientes/excluir.html",
        context,
    )