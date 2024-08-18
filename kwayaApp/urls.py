from django.urls import path
from . import views

urlpatterns = [
    path('kwaya', views.kwaya_page, name='kwaya'),
    path('achievements/', views.achievements_view, name='achievements'),
    ###############################
    path('member/transaction/create/', views.kwaya_member_transaction_create, name='kwaya-transaction-create'),
    path('member/transaction/list/', views.kwaya_member_transaction_list, name='kwaya-transaction-list'),
    path('member/transaction/update/<int:pk>/', views.kwaya_member_transaction_update, name='kwaya-transaction-update'),
    path('member/transaction/delete/<int:pk>/', views.kwaya_member_transaction_delete, name='kwaya-transaction-delete'),
    path('kwaya/member/<int:member_pk>/transactions/', views.kwaya_member_transaction_details, name='kwaya-member-transaction-details'),
    path('kwaya-members/', views.kwaya_member_list, name='kwaya-member-list'),
    path('kwaya-transactions/individuals/', views.individual_transactions, name='kwaya-individual-transactions'),
    
    
    path('kwaya-members/<int:member_id>/assign-voice/', views.create_voice_assignment, name='create-voice-assignment'),
    path('voice-assignments/<int:assignment_id>/update/', views.update_voice_assignment, name='update-voice-assignment'),
    path('voice-assignments/<int:assignment_id>/delete/', views.delete_voice_assignment, name='delete-voice-assignment'),
]
