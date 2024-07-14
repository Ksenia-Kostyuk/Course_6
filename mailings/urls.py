from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import base

app_name = MailingsConfig.name

urlpatterns = [
    path('', base),
]