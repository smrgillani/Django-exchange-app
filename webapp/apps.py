from django.apps import AppConfig


class WebAppConfig(AppConfig):
    name = 'webapp'

    def ready(self):
        print("Django Signals Ready!")
        from . import signals
