from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import MessagesListView, MessagesDetailView, MessagesCreateView, MessagesUpdateView, \
    MessagesDeleteView

app_name = MailingsConfig.name

urlpatterns = [
    path('', MessagesListView.as_view(), name='messages_list'),
    path('mailing/<int:pk>/', MessagesDetailView.as_view(), name='messages_detail'),
    path('create/', MessagesCreateView.as_view(), name='messages_create'),
    path('edit/<int:pk>/', MessagesUpdateView.as_view(), name='messages_update'),
    path('delete/<int:pk>/', MessagesDeleteView.as_view(), name='messages_delete'),
]