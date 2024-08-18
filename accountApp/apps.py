from django.apps import AppConfig


class AccountappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accountApp'
    verbose_name = 'User Account'
    order = 6