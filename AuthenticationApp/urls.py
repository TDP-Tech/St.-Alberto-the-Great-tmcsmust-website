from django.urls import path
from .views import member_list, member_detail, member_update, member_delete, register_member

urlpatterns = [
    #################################
    path('register/', register_member, name='register-member'),
    path('member/list/', member_list, name='member-list'),
    path('member/detail/<int:pk>/', member_detail, name='member-detail'),
    path('member/update/<int:pk>/', member_update, name='member-update'),
    path('member/delete/<int:pk>/', member_delete, name='member-delete'),
    #################################
    

]
