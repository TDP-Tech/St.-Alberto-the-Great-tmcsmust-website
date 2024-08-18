from django.urls import path
from . import views

urlpatterns=[
    path('create/', views.sadaka_create, name='sadaka-create'),
    path('sadaka-list/', views.sadaka_list, name='sadaka-list'),
    path('sadaka/<int:pk>/update/', views.sadaka_update, name='sadaka-update'),
    path('sadaka/<int:pk>/delete/', views.sadaka_delete, name='sadaka-delete'),
    ##########################
    path('mapato/', views.mapato, name='mapato'),
    path('mapatodemo/', views.mapatodemo, name='mapatodemo'),
]