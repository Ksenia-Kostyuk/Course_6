from random import sample

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.views.generic import TemplateView

from blog.models import MyBlog
from mailings.forms import MailingsForm, MessagesForm, MailingsModeratorForm, ClientsForm
from mailings.models import Messages, Mailings, Clients


class BaseView(TemplateView):
    template_name = 'mailings/base.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        mailings = Mailings.objects.all()
        blog = MyBlog.objects.all()
        context_data['all_mailings'] = mailings.count()
        context_data['blog_list'] = blog
        return context_data


class MessagesListView(ListView):
    model = Messages


class MessagesDetailView(DetailView):
    model = Messages


class MessagesCreateView(CreateView):
    model = Messages
    form_class = MessagesForm
    success_url = reverse_lazy('mailings:base')

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.owner = user
        message.save()
        return super().form_valid(form)


class MessagesUpdateView(UpdateView):
    model = Messages
    form_class = MessagesForm
    success_url = reverse_lazy('mailings:base')


class MessagesDeleteView(DeleteView):
    model = Messages
    success_url = reverse_lazy('mailings:base')


class MailingsListView(ListView):
    model = Mailings


class MailingsDetailView(DetailView):
    model = Mailings


class MailingsCreateView(CreateView):
    model = Mailings
    form_class = MailingsForm
    success_url = reverse_lazy('mailings:base')

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.owner = user
        mailing.save()
        return super().form_valid(form)


class MailingsUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailings
    form_class = MailingsForm
    success_url = reverse_lazy('mailings:base')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return MailingsForm
        if user.has_perm('mailings.can_unplug_mailings'):
            return MailingsModeratorForm
        raise PermissionDenied


class MailingsDeleteView(DeleteView):
    model = Mailings
    success_url = reverse_lazy('mailings:base')


def count_mail(request):
    """
    Возвращает общее число рассылок
    """
    context = Mailings.objects.all()
    return render(request, 'mailings/mailings_list.html', context)


class ClientsCreateView(CreateView):
    model = Clients
    form_class = ClientsForm
    success_url = reverse_lazy('mailings:base')

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)
