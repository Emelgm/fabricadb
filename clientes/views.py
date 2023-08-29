from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from .models import Cliente, Proveedor
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ClienteForm, ProveedorForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.models import User

############## Clientes
@login_required(login_url='remisiones:login')
def listar_clientes(request):
    if request.user.is_superuser:
        context = {}
        queryset = request.GET.get('buscar')
        clientes = Cliente.objects.filter(estado=True)
        if queryset:
            clientes = Cliente.objects.filter(
                Q(codigo__icontains = queryset) |
                Q(nombre__icontains = queryset),
                estado = True
            ).distinct()
            context['clientes'] = clientes
        paginator = Paginator(clientes, 10)
        page = request.GET.get('page')
        clientes = paginator.get_page(page)
        context['clientes'] = clientes
        return render(request, 'clientes/home.html', context)
    else:
         return redirect('remisiones:login')


class CrearCliente(CreateView):
    model = Cliente
    template_name = 'clientes/create.html'
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:list_clientes')


class ActualizarCliente(UpdateView):
    model = Cliente
    template_name = 'clientes/cliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:list_clientes')


class EliminarCliente(DeleteView):
    model = Cliente
    template_name = 'clientes/delete.html'

    def post(self, request, pk, *args, **kwargs):
        obj = Cliente.objects.get(id=pk)
        obj.estado = False
        obj.save()
        return redirect('clientes:list_clientes')


############# Proveedores
@login_required(login_url='remisiones:login')
def listar_proveedores(request):
    if request.user.is_superuser:
        context = {}
        queryset = request.GET.get('buscar')
        proveedores = Proveedor.objects.filter(estado=True)
        if queryset:
            proveedores = Proveedor.objects.filter(
                Q(nombre__icontains = queryset),
                estado = True
            ).distinct()
            context['proveedores'] = proveedores
        paginator = Paginator(proveedores, 10)
        page = request.GET.get('page')
        proveedores = paginator.get_page(page)
        context['proveedores'] = proveedores
        return render(request, 'proveedores/home.html', context)
    else:
         return redirect('remisiones:login')


class CrearProveedor(CreateView):
    model = Proveedor
    template_name = 'proveedores/create.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('clientes:list_proveedores')


class ActualizarProveedor(UpdateView):
    model = Proveedor
    template_name = 'proveedores/proveedor.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('clientes:list_proveedores')


class EliminarProveedor(DeleteView):
    model = Proveedor
    template_name = 'proveedores/delete.html'

    def post(self, request, pk, *args, **kwargs):
        obj = Proveedor.objects.get(id=pk)
        obj.estado = False
        obj.save()
        return redirect('clientes:list_proveedores')
    

############## Usuarios
def listar_user(request):
    if request.user.is_superuser:
        context = {}
        users = User.objects.filter(is_active=True)
        paginator = Paginator(users, 10)
        page = request.GET.get('page')
        users = paginator.get_page(page)
        context['usuarios'] = users
        return render(request, 'usuarios/home.html', context)
    else:
         return redirect('remisiones:login')


class EliminarUser(DeleteView):
    model = User
    template_name = 'usuarios/delete.html'

    def post(self, request, pk, *args, **kwargs):
        obj = User.objects.get(id=pk)
        obj.is_active = False
        obj.save()
        return redirect('clientes:users')