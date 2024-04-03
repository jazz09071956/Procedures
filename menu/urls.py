from django.urls import path
from . import views
urlpatterns =[
    path('', views.HomeView.as_view(), name='home_view'),
    path('hola', views.VistaFormulario.as_view(), name='vistaformulario'),
]
