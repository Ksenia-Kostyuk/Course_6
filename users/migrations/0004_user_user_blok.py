# Generated by Django 4.2.2 on 2024-07-18 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_blok',
            field=models.BooleanField(default=False, verbose_name='Блокировка пользователя'),
        ),
    ]
