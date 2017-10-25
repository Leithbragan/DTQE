from django.contrib.auth.models import User
from django.db import models


class SimpleUser(models.Model):
    class Meta:
        verbose_name = u'пользователь'
        verbose_name_plural = u'пользователи'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=u'пользователь')
    moder = models.BooleanField(default=False, verbose_name=u'модератор')

    def __str__(self):
        return '%s' % self.user.first_name



