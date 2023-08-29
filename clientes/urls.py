from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

app_name = 'clientes'
urlpatterns = [
    # clientes
    path('', listar_clientes, name='list_clientes'),
    path('agregar_cliente/', login_required(CrearCliente.as_view()), name='add_cliente'),
    path('editar_cliente/<int:pk>/', login_required(ActualizarCliente.as_view()), name='edit_cliente'),
    path('<int:pk>/', login_required(EliminarCliente.as_view()), name='del_cliente'),
    # proveedores
    path('proveedores/', listar_proveedores, name='list_proveedores'),
    path('agregar_proveedor/', login_required(CrearProveedor.as_view()), name='add_proveedor'),
    path('editar_proveedor/<int:pk>/', login_required(ActualizarProveedor.as_view()), name='edit_proveedor'),
    path('proveedor/<int:pk>/', login_required(EliminarProveedor.as_view()), name='del_proveedor'),
    # usuarios
    path('usuarios/', listar_user, name='users'),
    path('eliminar_user/<int:pk>/', login_required(EliminarUser.as_view()), name='del_user'),
]