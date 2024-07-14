from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailings.models import Messages, Mailings


class MessagesListView(ListView):
    model = Messages


class MessagesDetailView(DetailView):
    model = Messages


class MessagesCreateView(CreateView):
    model = Messages
    fields = ('theme', 'body')
    success_url = reverse_lazy('mailings:messages_list')


class MessagesUpdateView(UpdateView):
    model = Messages
    fields = ('theme', 'body')
    success_url = reverse_lazy('mailings:messages_list')


class MessagesDeleteView(DeleteView):
    model = Messages
    success_url = reverse_lazy('mailings:messages_list')


class MailingsListView(ListView):
    model = Mailings


class MailingsDetailView(DetailView):
    model = Mailings


class MailingsCreateView(CreateView):
    model = Mailings
    fields = ('id', 'date', 'frequency', 'status', 'message')
    success_url = reverse_lazy('mailings:messages_list')


class MailingsUpdateView(UpdateView):
    model = Mailings
    fields = ('id', 'date', 'frequency', 'status', 'message')
    success_url = reverse_lazy('mailings:messages_list')


class MailingsDeleteView(DeleteView):
    model = Mailings
    success_url = reverse_lazy('mailings:messages_list')
