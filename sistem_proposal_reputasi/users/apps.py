import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "sistem_proposal_reputasi.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import sistem_proposal_reputasi.users.signals  # noqa: F401
