from django.urls import path
from . import views

urlpatterns = [
    path('legio-maria/', views.legio_page, name='legio-maria'),
    ###############################
    path('member/transaction/create/', views.legio_member_transaction_create, name='legio-transaction-create'),
    path('member/transaction/list/', views.legio_member_transaction_list, name='legio-transaction-list'),
    path('member/transaction/update/<int:pk>/', views.legio_member_transaction_update, name='legio-transaction-update'),
    path('member/transaction/delete/<int:pk>/', views.legio_member_transaction_delete, name='legio-transaction-delete'),
    path('legio/member/<int:member_pk>/transactions/', views.legio_member_transaction_details, name='legio-member-transaction-details'),
    path('legio-members/', views.legio_member_list, name='legio-member-list'),
    path('legio-transactions/individuals/', views.individual_transactions, name='legio-individual-transactions'),
]
