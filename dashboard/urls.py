from django.urls import path
from dashboard import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',login_required(views.home), name="home"),
    path('estadisticas/', views.estadisticas, name="estadisticas"),
    path('busqueda/', views.busqueda, name="busqueda"),
    path('graficos/', views.graficos, name="graficos"),
]
