from django.db import models


class Messages(models.Model):
    objects = None
    theme = models.CharField(max_length=100, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Сообщение')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'{self.theme}'
