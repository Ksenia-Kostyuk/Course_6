from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    tg_name = models.CharField(max_length=50, verbose_name='Ник пользователя')
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Аватар', blank=True, null=True)
    user_blok = models.BooleanField(default=False, verbose_name='Блокировка пользователя')

    token = models.CharField(max_length=100, verbose_name='Токен', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions = [
            ('can_blok_users', 'Может заблокировать пользователя'),
            ('can_see_users', 'Может посмотреть список пользователей')
        ]

    def __str__(self):
        return self.email