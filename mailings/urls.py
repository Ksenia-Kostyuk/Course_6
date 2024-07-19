from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import MailingsListView, MailingsDetailView, MailingsCreateView, MailingsUpdateView, \
    MailingsDeleteView, MessagesDetailView, count_mail

app_name = MailingsConfig.name

urlpatterns = [
    path('', MailingsListView.as_view(), name='mailings_list'),
    path('mailing/<int:pk>/', MailingsDetailView.as_view(), name='mailings_detail'),
    path('create/', MailingsCreateView.as_view(), name='mailings_create'),
    path('edit/<int:pk>/', MailingsUpdateView.as_view(), name='mailings_update'),
    path('delete/<int:pk>/', MailingsDeleteView.as_view(), name='mailings_delete'),
    path('mailing/<int:pk>/', MessagesDetailView.as_view(), name='messages_detail'),
    path('', count_mail, name='count')
]