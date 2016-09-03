from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.validators import ASCIIUsernameValidator, UnicodeUsernameValidator
from djangae.contrib.gauth.datastore.models import GaeAbstractDatastoreUser
from django.utils import six
from django.utils.translation import ugettext_lazy as _


class DatastoreUser(GaeAbstractDatastoreUser):
    username_validator = UnicodeUsernameValidator() if six.PY3 else ASCIIUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    #email = models.EmailField(_('email address'), blank=True)

    class Meta:
        app_label = "users"
        swappable = 'AUTH_USER_MODEL'
        verbose_name = _('user')
        verbose_name_plural = _('users')
