from django.urls import path
from dashboard import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',login_required(views.home), name="home"),
    path('estadisticas/', login_required(views.estadisticas), name="estadisticas"),
    path('busqueda/', login_required(views.busqueda), name="busqueda"),
    path('graficos/', login_required(views.graficos), name="graficos"),
]
