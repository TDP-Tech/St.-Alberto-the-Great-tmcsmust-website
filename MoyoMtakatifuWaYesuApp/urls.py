from django.urls import path
from . import views

urlpatterns = [
    path('moyomtakatifuwaYesu/', views.moyomtakatifuwaYesu_page, name='moyomtakatifuwaYesu'),
    ###############################
    path('member/transaction/create/', views.moyomtakatifuwaYesu_member_transaction_create, name='moyomtakatifuwaYesu-transaction-create'),
    path('member/transaction/list/', views.moyomtakatifuwaYesu_member_transaction_list, name='moyomtakatifuwaYesu-transaction-list'),
    path('member/transaction/update/<int:pk>/', views.moyomtakatifuwaYesu_member_transaction_update, name='moyomtakatifuwaYesu-transaction-update'),
    path('member/transaction/delete/<int:pk>/', views.moyomtakatifuwaYesu_member_transaction_delete, name='moyomtakatifuwaYesu-transaction-delete'),
    path('moyomtakatifuwaYesu/member/<int:member_pk>/transactions/', views.moyomtakatifuwaYesu_member_transaction_details, name='moyomtakatifuwaYesu-member-transaction-details'),
    path('moyomtakatifuwaYesu-members/', views.moyomtakatifuwaYesu_member_list, name='moyomtakatifuwaYesu-member-list'),
    path('moyomtakatifuwaYesu-transactions/individuals/', views.individual_transactions, name='moyomtakatifuwaYesu-individual-transactions'),
]
