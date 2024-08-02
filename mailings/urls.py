from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import MailingsListView, MailingsDetailView, MailingsCreateView, MailingsUpdateView, \
    MailingsDeleteView, MessagesDetailView, count_mail, MessagesCreateView, MessagesUpdateView, BaseView, \
    ClientsCreateView

app_name = MailingsConfig.name

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('list/', MailingsListView.as_view(), name='mailings_list'),
    path('mailing/<int:pk>/', MailingsDetailView.as_view(), name='mailings_detail'),
    path('create/', MailingsCreateView.as_view(), name='mailings_create'),
    path('edit/<int:pk>/', MailingsUpdateView.as_view(), name='mailings_update'),
    path('delete/<int:pk>/', MailingsDeleteView.as_view(), name='mailings_delete'),
    path('mailing/<int:pk>/', MessagesDetailView.as_view(), name='messages_detail'),
    path('create/', MessagesCreateView.as_view(), name='messages_create'),
    path('edit/<int:pk>/', MessagesUpdateView.as_view(), name='messages_update'),
    path('<int:pk>/', MessagesDetailView.as_view(), name='messages_detail'),
    path('create/', ClientsCreateView.as_view(), name='clients_create'),
    path('', count_mail, name='count')
]