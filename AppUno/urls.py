from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('luis',views.luis, name="luis" ),
    path('datos', views.datos, name="datos"),
    path('ventas', views.conpag, name="conpag"),
    path('servicios', views.servicios, name="servicios" ),
    path('about', views.about, name="about")

]
