from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ConstanceConfig(AppConfig):
    name = 'constance'
    verbose_name = _('Constance')

    def ready(self):
        from . import connect
