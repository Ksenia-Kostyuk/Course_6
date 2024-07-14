from django.contrib import admin

from mailings.models import Messages


@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('theme', 'body')
