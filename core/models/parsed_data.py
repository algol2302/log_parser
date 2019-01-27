# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ParsedData(models.Model):
    ip_addr = models.GenericIPAddressField(verbose_name=_('IP'))

    log_date = models.DateTimeField(verbose_name=_('Дата'))

    http_method = models.CharField(verbose_name=_('Нttp метод'), max_length=10)

    uri = models.TextField(verbose_name=_('URI'))

    error_code = models.PositiveIntegerField(
        verbose_name=_('Код ошибки'), default=0
    )

    response_size = models.PositiveIntegerField(
        verbose_name=_('Размер ответа')
    )

    other = models.TextField(verbose_name=_('Текст строки'))

    class Meta:
        verbose_name = _('Распарсенные данные')
        verbose_name_plural = _('Распарсенные данные')

    def __str__(self):
        return "{} {}".format(self.id, self.log_date)
