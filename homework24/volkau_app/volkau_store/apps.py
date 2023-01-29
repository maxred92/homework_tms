from django.apps import AppConfig


class VolkauStoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'volkau_store'


    def ready(self):
        from volkau_store import signals
