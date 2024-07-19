from django.db import models


class MyBlog(models.Model):
    name = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(blank=True, null=True, verbose_name='Содержимое')
    image = models.ImageField(upload_to='blog', blank=True, null=True, verbose_name='Изображение')
    date_create = models.DateField(blank=True, null=True, verbose_name='Дата создания')
    publication_sign = models.BooleanField(default=False, verbose_name='Признак публикации')
    views_counter = models.PositiveIntegerField(default=0, verbose_name='Просмотры', help_text='Количество просмотров')

    class Meta:
        verbose_name = 'Заголовок'
        verbose_name_plural = 'Заголовки'

    def __str__(self):
        return f'{self.name}'
