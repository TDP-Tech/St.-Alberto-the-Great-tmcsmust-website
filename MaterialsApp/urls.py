from django.urls import path
from .views import all_materials, filter_materials
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('add/', views.add_material, name='add-material'),
    path('all/', all_materials, name='all-materials'),
    path('<str:level>/', filter_materials, name='filter-materials'),
    path('edit/<int:material_id>/', views.edit_material, name='edit-material'),
    path('delete/<int:material_id>/', views.delete_material, name='delete-material'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)