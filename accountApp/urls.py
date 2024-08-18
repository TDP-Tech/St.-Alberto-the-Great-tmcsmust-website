# accounts/urls.py
from django.urls import path
from .views import signup_view, login_view, logout_view, user_list_view
from .views import profile_list, profile_detail, profile_create, profile_update, profile_delete
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('users/', user_list_view, name='user-list'),
    
    # Password Reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    #profiles urls
    path('profiles/', profile_list, name='profile-list'),
    path('profiles/create/', profile_create, name='profile-create'),
    path('profiles/<int:pk>/', profile_detail, name='profile-detail'),
    path('profiles/<int:pk>/update/', profile_update, name='profile-update'),
    path('profiles/<int:pk>/delete/', profile_delete, name='profile-delete'),
]
