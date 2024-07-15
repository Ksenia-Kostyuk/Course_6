from datetime import timezone

from django.db import models


class Messages(models.Model):
    theme = models.CharField(max_length=100, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Сообщение')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'{self.theme}'


class Clients(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email')
    name = models.CharField(max_length=200, verbose_name='ФИО')
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.name}'


class Mailings(models.Model):
    STATUS_CHOICES = [('создано', 'Создано'), ('начато', 'Начато'), ('завершено', 'Завершено')]
    date = models.DateTimeField(verbose_name='Дата и время первой рассылки')

    e = models.DateTimeField(verbose_name='Дата и время окончания рассылки')
    frequency = models.CharField(max_length=100, choices=[('ежедневно', 'Ежедневно'), ('еженедельно', 'Еженедельно'),
                                                          ('ежемесячно', 'Ежемесячно')],
                                 verbose_name='Периодичность')
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, verbose_name='Статус')
    message = models.OneToOneField(Messages, on_delete=models.CASCADE)
    clients = models.ManyToManyField(Clients)

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    def __str__(self):
        return f'{self.id} - {self.status}'


class Сhance(models.Model):
    mailing = models.ForeignKey(Mailings, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время последней попытки рассылки')
    status = models.CharField(max_length=100, choices=[('успешно', 'Успешно'), ('сбой', 'Сбой')], verbose_name='Статус')
    response = models.TextField(blank=True, null=True, verbose_name='Ответ сервера')

    class Meta:
        verbose_name = 'Попытка'
        verbose_name_plural = 'Попытки'

    def __str__(self):
        return f'{self.id} - {self.status}'
