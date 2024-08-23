# urls.py (inside the class_leader app)

from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_class_leader, name='create'),
    # path('leaders-list/', views.leader_list, name='leader-list'),
    path('leaders/<str:role>/', views.leader_list, name='leader_list'),
    path('update/<int:pk>/', views.update_class_leader, name='update'),
    path('delete/<int:pk>/', views.delete_class_leader, name='delete'),
    path('class-members/', views.class_members, name='class-members'),
]

