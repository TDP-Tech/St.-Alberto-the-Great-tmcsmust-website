from django.urls import path
from . import views


urlpatterns = [
    path('transaction/create/', views.member_transaction_create, name='transaction-create'),
    path('transaction/list/', views.member_transaction_list, name='transaction-list'),
    path('transaction/update/<int:pk>/', views.member_transaction_update, name='transaction-update'),
    path('transaction/delete/<int:pk>/', views.member_transaction_delete, name='transaction-delete'),
    path('transactions/<int:member_id>/', views.individual_member_transaction_details, name='individual-member-transactions-details'),
    path('transactions/individual/', views.individual_transactions, name='individual-transactions'),

]
