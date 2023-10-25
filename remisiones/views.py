from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib import messages
# from django.shortcuts import render_to_response
# from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from productos.models import Producto, RemiProd
from .carrito import Carrito
from .models import Remisiones
from .forms import RemisionForm, CreateUserForm
from .utils import render_to_pdf


# ##### error 404
# def handler_404(request, *args, **kwargs):
#     response = render_to_response(
#         '404.html',
#         {},
#         context_instance=RequestContext(request)
#     )
#     response.status_code = 404
#     return response

############## Login
def registro(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La cuenta fue creada')
            return redirect('remisiones:login')
    context = {
        'form': form
    }
    return render(request, 'registro.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('remisiones:list_remisiones')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('remisiones:list_remisiones')
            else:
                messages.info(request, 'Usuario o Contraseña incorrecta')
        context = {}
        return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('remisiones:login')


############# remisiones
@login_required(login_url='remisiones:login')
def listar_remisiones(request):
    context = {}
    queryset = request.GET.get('buscar')
    inicio = request.GET.get('inicio')
    final = request.GET.get('final')
    remisiones = Remisiones.objects.all().order_by('-created')
    if queryset:
        remisiones = Remisiones.objects.filter(
            Q(codigo__icontains = queryset)
        ).distinct()
        context['remisiones'] = remisiones
    if inicio and final:
        remisiones = Remisiones.objects.filter(
            Q(fecha_despacho__range = [inicio, final])
        ).distinct()
        context['remisiones'] = remisiones
    paginator = Paginator(remisiones, 10)
    page = request.GET.get('page')
    remisiones = paginator.get_page(page)
    context['remisiones'] = remisiones
    return render(request, 'remisiones/home.html', context)

@login_required(login_url='remisiones:login')
def agregar_remision(request):
    if request.user.is_superuser:
        limpiar_carrito(request)
        context = {}
        form = RemisionForm(request.POST or None)
        if form.errors:
            return render(request, '404.html')
        elif form.is_valid():
            form.save()
            return remisiones(request)
        context['form'] = form
        return render(request, 'remisiones/create.html', context)
    else:
         return redirect('remisiones:login')


class EliminarResmision(DeleteView):
    model = Remisiones
    template_name = 'remisiones/delete.html'
    success_url = reverse_lazy('remisiones:list_remisiones')


@login_required(login_url='remisiones:login')
def despachar(request, pk):
    obj = get_object_or_404(Remisiones, id=pk)
    if obj.orden == False:
        obj.orden = True
        obj.usuario = request.user.username
        obj.save()
    return redirect('remisiones:list_remisiones')

@login_required(login_url='remisiones:login')
def eliminar_remision(request, remision_id):
    if request.user.is_superuser:
        remision = get_object_or_404(Remisiones, id=remision_id)
        if request.method =="POST":
            remision.delete()
            return redirect('remisiones:list_remisiones')
        context = {
            'remision':remision
            }
        return render(request, 'remisiones/delete.html', context)
    else:
         return redirect('remisiones:login')

@login_required(login_url='remisiones:login')
def detalle(request, pk):
    remision = Remisiones.objects.get(id=pk)
    detail = RemiProd.objects.filter(remision_id=pk)
    total_c = 0
    for i in detail:
        total_c += i.cantidad
    context = {
        'detalles': detail,
        'remision': remision,
        'total_c': total_c
    }
    return render(request, 'remisiones/detalle.html', context)

def export_pdf(request, pk):
    remision = Remisiones.objects.get(id=pk)
    detail = RemiProd.objects.filter(remision_id=pk)
    total_p = 0
    total_c = 0
    for i in detail:
        total_c += i.cantidad
    context = {
        'detalles': detail,
        'remision': remision,
        'total_c': total_c
    }
    pdf = render_to_pdf('remisiones/exportpdf.html', context)
    return HttpResponse(pdf, content_type='application/pdf')


##################### carrito ######################
@login_required(login_url='remisiones:login')
def remisiones(request):
    if request.user.is_superuser:
        context = {}
        remidion_id = Remisiones.objects.order_by('id').last()
        queryset = request.GET.get('buscar')
        productos = Producto.objects.filter(estado=True)
        if queryset:
            productos = Producto.objects.filter(
                Q(codigo__icontains = queryset) |
                Q(nombre__icontains = queryset) |
                Q(marca__icontains = queryset),
                estado = True
            ).distinct()
            context['productos'] = productos
        paginator = Paginator(productos, 10)
        page = request.GET.get('page')
        productos = paginator.get_page(page)
        context['productos'] = productos
        context['remidion_id'] = remidion_id
        return render(request, 'remisiones.html', context)
    else:
         return redirect('remisiones:login')

@login_required(login_url='remisiones:login')
def agregar_producto(request, producto_id):
    if request.user.is_superuser:
        carrito = Carrito(request)
        producto = Producto.objects.get(id=producto_id)
        carrito.agregar(producto)
        return redirect('remisiones:rem')
    else:
         return redirect('remisiones:login')

@login_required(login_url='remisiones:login')
def eliminar_producto(request, producto_id):
    if request.user.is_superuser:
        carrito = Carrito(request)
        producto = Producto.objects.get(id=producto_id)
        carrito.eliminar(producto)
        return redirect('remisiones:rem')
    else:
         return redirect('remisiones:login')

@login_required(login_url='remisiones:login')
def restar_producto(request, producto_id):
    if request.user.is_superuser:
        carrito = Carrito(request)
        producto = Producto.objects.get(id=producto_id)
        carrito.restar(producto)
        return redirect('remisiones:rem')
    else:
         return redirect('remisiones:login')

@login_required(login_url='remisiones:login')
def limpiar_carrito(request):
    if request.user.is_superuser:
        carrito = Carrito(request)
        carrito.limpiar()
        return redirect('remisiones:rem')
    else:
         return redirect('remisiones:login')

@login_required(login_url='remisiones:login')
def save_carrito(request):
    if request.user.is_superuser:
        remidion_id = Remisiones.objects.order_by('id').last()
        carrito = request.session.get('carrito').values()
        for i in carrito:
            producto_id = Producto.objects.get(id=i['producto_id'])
            pedido = RemiProd(
                cantidad = int(i['cantidad']),
                remision_id = remidion_id,
                producto_id = producto_id
            )
            pedido.save()
            restar = Producto.objects.get(nombre=producto_id)
            restar.cantidad -= int(i['cantidad'])
            #restar.peso -= float(i['peso'])
            restar.save()
        limpiar_carrito(request)
        return redirect('remisiones:list_remisiones')
    else:
         return redirect('remisiones:login')