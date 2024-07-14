from django.contrib import admin

from mailings.models import Messages, Clients, Mailings, Сhance


@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('theme', 'body')


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'comment')


@admin.register(Mailings)
class MailingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'frequency', 'status', 'message')


@admin.register(Сhance)
class СhanceAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'date', 'status', 'response')
