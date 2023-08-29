from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

app_name = 'remisiones'
urlpatterns = [
    # login
    path('registro/', registro, name='registro'),
    path('login/', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
    # remisiones
    path('', listar_remisiones, name='list_remisiones'),
    path('agregar_remision/', agregar_remision, name='add_remision'),
    path('eliminar_remision/<int:pk>/', login_required(EliminarResmision.as_view()), name='del_remision'),
    path('<int:pk>/', despachar, name='despachar'),
    path('detalle_remision/<int:pk>', detalle, name='detail_remision'),
    path('pdf_remisiones/<int:pk>', export_pdf, name='pdf_rem'),
    # carrito
    path('carrito/', remisiones, name='rem'),
    path('agregar_carrito/<int:producto_id>/', agregar_producto, name='Add'),
    path('eliminar_carrito/<int:producto_id>/', eliminar_producto, name='Del'),
    path('restar_carrito/<int:producto_id>/', restar_producto, name='Sub'),
    path('limpiar_carrito/', limpiar_carrito, name='CLS'),
    path('guardar_carrito/', save_carrito, name='save')
]
