from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

app_name = 'productos'
urlpatterns = [
    path('', listar_productos, name='list_productos'),
    path('agregar_producto/', login_required(CrearProducto.as_view()), name='add_producto'),
    path('editar_producto/<int:pk>/', login_required(ActualizarProducto.as_view()), name='edit_producto'),
    path('<int:pk>/', login_required(EliminarProducto.as_view()), name='del_producto'),
    path('stock/', stock_pdf, name='stock'),
    # recepciones
    path('recepciones/', listar_recepciones, name='list_recepciones'),
    path('agregar_recepcion/', agregar_recepcion, name='add_recepcion'),
    path('eliminar_recepcion/<int:pk>/', login_required(EliminarRecepcion.as_view()), name='del_recepcion'),
    path('recepcion/<int:pk>/', recepcionar, name='recepcionar'),
    path('detalle_recepcion/<int:pk>', detalle, name='detail_recepcion'),
    path('pdf_recepciones/<int:pk>', export_pdf, name='pdf_recep'),
    # carrito
    path('recepcion/', recepciones, name='recep'),
    path('add_recepcion/<int:producto_id>/', agregar_producto, name='Add'),
    path('del_recepcion/<int:producto_id>/', eliminar_producto, name='Del'),
    path('sub_recepcion/<int:producto_id>/', restar_producto, name='Sub'),
    path('clear_recepcion/', limpiar_carrito, name='CLS'),
    path('guardar_recepcion/', save_recepcion, name='save')
]