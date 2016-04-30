from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

User = settings.AUTH_USER_MODEL


@python_2_unicode_compatible
class UserProfile(models.Model):

    """
    Model used to store more information on users
    """
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    user = models.OneToOneField(User, verbose_name=_("User"))

    def __str__(self):
        return _("{user}'s profile").format(user=self.user)


# S I G N A L S
from users import signals
