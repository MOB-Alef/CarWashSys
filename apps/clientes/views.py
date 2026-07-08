from django.shortcuts import render, redirect

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