from django.apps import AppConfig


class BaseApisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_apis'
