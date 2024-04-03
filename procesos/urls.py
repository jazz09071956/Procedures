from django.urls import path
from django.contrib.auth import views as auth_views
from procesos import views as views1

#JJ 
urlpatterns =[

    #path para listar procesos
    path('procesos/', views1.ProcesoList.as_view(), name='proceso_listado'),
    #path para ver detalles de proceso
    path('proceso/<int:pk>/', views1.ProcesoDetail.as_view(), name='proceso_extendido'),
    #path para adicionar proceso
    path('proceso/adicionar/', views1.ProcesoCreate.as_view(), name='proceso_adicionar'),
    #path para Editar proceso
    path('proceso/<int:pk>/editar/', views1.ProcesoUpdate.as_view(), name='proceso_editar'),

    #path para listar detalle de procesos
    path('proceso/<int:parent_pk>/detalles/', views1.Detalle_ProcesoList.as_view(), name='detalle_proceso_listado'),
    #path para ver detalle de detalle de proceso
    path('proceso/<int:parent_pk>/detalle/<int:pk>/', views1.Detalle_ProcesoDetail.as_view(), name='detalle_proceso_extendido'),
    #path para adicionar detalle proceso
    path('proceso/<int:parent_pk>/detalle/adicionar/', views1.Detalle_ProcesoCreate.as_view(), name='detalle_proceso_adicionar'),
    #path para Editar detalle de proceso
    path('proceso/<int:parent_pk>/detalle/<int:pk>/editar/', views1.Detalle_ProcesoUpdate.as_view(), name='detalle_proceso_editar'),
    #path para Eliminar detalle de proceso
    path('proceso/<int:parent_pk>/detalle/<int:pk>/eliminar/',views1.Detalle_ProcesoDelete.as_view(), name='detalle_proceso_eliminar'),

]
