# Generated by Django 4.2.2 on 2024-07-17 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0004_remove_mailings_message_messages_mailing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='mailing',
        ),
        migrations.AddField(
            model_name='mailings',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message', to='mailings.messages'),
        ),
    ]
