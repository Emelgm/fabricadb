from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Producto, Recepcion, ReceProd
from .forms import ProductoForm, RecepcionForm
from remisiones.carrito import Carrito
from remisiones.utils import render_to_pdf

@login_required(login_url='remisiones:login')
def listar_productos(request):
    if request.user.is_superuser:
        context = {}
        queryset = request.GET.get('buscar')
        productos = Producto.objects.filter(estado=True).order_by('-codigo')
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
        return render(request, 'productos/home.html', context)
    else:
         return redirect('remisiones:login')


class CrearProducto(CreateView):
    model = Producto
    template_name = 'productos/create.html'
    form_class = ProductoForm
    success_url = reverse_lazy('productos:list_productos')


class ActualizarProducto(UpdateView):
    model = Producto
    template_name = 'productos/producto.html'
    form_class = ProductoForm
    success_url = reverse_lazy('productos:list_productos')


class EliminarProducto(DeleteView):
    model = Producto
    template_name = 'productos/delete.html'

    def post(self, request, pk, *args, **kwargs):
        obj = Producto.objects.get(id=pk)
        obj.estado = False
        obj.save()
        return redirect('productos:list_productos')
    

############# Recepcion
@login_required(login_url='remisiones:login')
def listar_recepciones(request):
    context = {}
    inicio = request.GET.get('inicio')
    final = request.GET.get('final')
    recepciones = Recepcion.objects.all().order_by('-fecha_recepcion')
    if inicio and final:
        recepciones = Recepcion.objects.filter(
            Q(fecha_recepcion__range = [inicio, final])
        ).distinct()
        context['recepciones'] = recepciones
    paginator = Paginator(recepciones, 10)
    page = request.GET.get('page')
    recepciones = paginator.get_page(page)
    context['recepciones'] = recepciones
    return render(request, 'recepciones/home.html', context)


@login_required(login_url='remisiones:login')
def agregar_recepcion(request):
    if request.user.is_superuser:
        context = {}
        form = RecepcionForm(request.POST or None)
        if form.is_valid():
            form.save()
            return recepciones(request)
        context['form'] = form
        return render(request, 'recepciones/create.html', context)
    else:
         return redirect('remisiones:login')


class EliminarRecepcion(DeleteView):
    model = Recepcion
    template_name = 'recepciones/delete.html'
    success_url = reverse_lazy('productos:list_recepciones')


@login_required(login_url='remisiones:login')
def detalle(request, pk):
    recepcion = Recepcion.objects.get(id=pk)
    detail = ReceProd.objects.filter(recepcion_id=pk)
    total_c = 0
    for i in detail:
        total_c += i.cantidad
    context = {
        'detalles': detail,
        'recepcion': recepcion,
        'total_c': total_c
    }
    return render(request, 'recepciones/detalle.html', context)


def export_pdf(request, pk):
    recepcion = Recepcion.objects.get(id=pk)
    detail = ReceProd.objects.filter(recepcion_id=pk)
    total_c = 0
    for i in detail:
        total_c += i.cantidad
    context = {
        'detalles': detail,
        'recepcion': recepcion,
        'total_c': total_c
    }
    pdf = render_to_pdf('recepciones/exportpdf.html', context)
    return HttpResponse(pdf, content_type='application/pdf')


def stock_pdf(request):
    productos = Producto.objects.filter(estado=True).order_by('codigo')
    total_c = 0
    total_p = productos.count()
    for i in productos:
        total_c += i.cantidad
    context = {
        'productos': productos,
        'total_c': total_c,
        'total_p': total_p
    }
    pdf = render_to_pdf('productos/stock.html', context)
    return HttpResponse(pdf, content_type='application/pdf')


@login_required(login_url='remisiones:login')
def recepcionar(request, pk):
    obj = get_object_or_404(Recepcion, id=pk)
    if obj.orden == False:
        obj.orden = True
        obj.usuario = request.user.username
        obj.save()
    return redirect('productos:list_recepciones')


##################### carrito ######################
@login_required(login_url='remisiones:login')
def recepciones(request):
    if request.user.is_superuser:
        context = {}
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
        return render(request, 'recepciones/recepcion.html', context)
    else:
         return redirect('remisiones:login')

@login_required(login_url='remisiones:login')
def agregar_producto(request, producto_id):
    if request.user.is_superuser:
        carrito = Carrito(request)
        producto = Producto.objects.get(id=producto_id)
        carrito.agregar(producto)
        return redirect('productos:recep')
    else:
         return redirect('remisiones:login')

@login_required(login_url='remisiones:login')
def eliminar_producto(request, producto_id):
    if request.user.is_superuser:
        carrito = Carrito(request)
        producto = Producto.objects.get(id=producto_id)
        carrito.eliminar(producto)
        return redirect('productos:recep')
    else:
         return redirect('remisiones:login')

@login_required(login_url='remisiones:login')
def restar_producto(request, producto_id):
    if request.user.is_superuser:
        carrito = Carrito(request)
        producto = Producto.objects.get(id=producto_id)
        carrito.restar(producto)
        return redirect('productos:recep')
    else:
         return redirect('remisiones:login')

@login_required(login_url='remisiones:login')
def limpiar_carrito(request):
    if request.user.is_superuser:
        carrito = Carrito(request)
        carrito.limpiar()
        return redirect('productos:recep')
    else:
         return redirect('remisiones:login')

@login_required(login_url='remisiones:login')
def save_recepcion(request):
    if request.user.is_superuser:
        recepcion_id = Recepcion.objects.order_by('id').last()
        carrito = request.session.get('carrito').values()
        for i in carrito:
            producto_id = Producto.objects.get(id=i['producto_id'])
            pedido = ReceProd(
                cantidad = int(i['cantidad']),
                recepcion_id = recepcion_id,
                producto_id = producto_id
            )
            pedido.save()
            sumar = Producto.objects.get(nombre=producto_id)
            sumar.cantidad += int(i['cantidad'])
            sumar.save()
        limpiar_carrito(request)
        return redirect('productos:list_recepciones')
    else:
         return redirect('remisiones:login')