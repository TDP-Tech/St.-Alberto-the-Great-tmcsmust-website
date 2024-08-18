from django.urls import path
from . import views

urlpatterns = [
    path('visakramenti/', views.mipangonafedhahomepage, name='mipango-home'),
    path('saloon/', views.saloon, name='saloon'),
    path('itservices/', views.itservices, name='itservices'),
    path('architecture/', views.architecture, name='architecture'),
    path('keki/', views.keki, name='keki'),
    path('mapambo/', views.mapambonasherehe, name='mapambo'),
    ###############
    path('mauzo/create/', views.mauzo_create, name='mauzo-create'),
    path('mauzo/list/', views.mauzo_list, name='mauzo-list'),
    path('mauzo/update/<int:pk>/', views.mauzo_update, name='mauzo-update'),
    path('mauzo/delete/<int:pk>/', views.mauzo_delete, name='mauzo-delete'),
    # path('mipango/', views.mipango, name='mapato-na-matumizi'),
    path('mapato-na-matumizi/', views.mapato_na_matumizi_report, name='mapato-na-matumizi'),
    path('mipangodemo/', views.mipangodemo3, name='mipangodemo'),
    path('report-ya-mapato-mipango-na-fedha/', views.report_mapato, name='report-ya-mapato-kamati-ya-mipango-na-fedha'),
    ################
    path('matumizi/create/', views.matumizi_create, name='matumizi-create'),
    path('matumizi/list/', views.matumizi_list, name='matumizi-list'),
    path('matumizi/update/<int:pk>/', views.matumizi_update, name='matumizi-update'),
    path('matumizi/delete/<int:pk>/', views.matumizi_delete, name='matumizi-delete'),
    path('report-ya-matumizi-mipango-na-fedha/', views.report_matumizi, name='report-ya-matumizi-kamati-ya-mipango-na-fedha'),
    
]
