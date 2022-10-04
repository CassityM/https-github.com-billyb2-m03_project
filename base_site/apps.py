from django.apps import AppConfig


class BaseSiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_site'
