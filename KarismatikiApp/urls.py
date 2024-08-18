from django.urls import path
from . import views

urlpatterns = [
    path('karismatiki/', views.karismatiki_page, name='karismatiki'),
    ###############################
    path('member/transaction/create/', views.karismatiki_member_transaction_create, name='karismatiki-transaction-create'),
    path('member/transaction/list/', views.karismatiki_member_transaction_list, name='karismatiki-transaction-list'),
    path('member/transaction/update/<int:pk>/', views.karismatiki_member_transaction_update, name='karismatiki-transaction-update'),
    path('member/transaction/delete/<int:pk>/', views.karismatiki_member_transaction_delete, name='karismatiki-transaction-delete'),
    path('karismatiki/member/<int:member_pk>/transactions/', views.karismatiki_member_transaction_details, name='karismatiki-member-transaction-details'),
    path('karismatiki-members/', views.karismatiki_member_list, name='karismatiki-member-list'),
    path('karismatiki-transactions/individuals/', views.individual_transactions, name='karismatiki-individual-transactions'),
]
