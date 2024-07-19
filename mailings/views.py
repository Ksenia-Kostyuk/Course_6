from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailings.forms import MailingsForm, MessagesForm, MailingsModeratorForm
from mailings.models import Messages, Mailings


class MessagesListView(ListView):
    model = Messages


class MessagesDetailView(DetailView):
    model = Messages


class MessagesCreateView(CreateView):
    model = Messages
    form_class = MessagesForm
    success_url = reverse_lazy('mailings:mailings_list')

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.owner = user
        message.save()
        return super().form_valid(form)


class MessagesUpdateView(UpdateView):
    model = Messages
    form_class = MessagesForm
    success_url = reverse_lazy('mailings:mailings_list')


class MessagesDeleteView(DeleteView):
    model = Messages
    success_url = reverse_lazy('mailings:mailings_list')


class MailingsListView(ListView):
    model = Mailings


class MailingsDetailView(DetailView):
    model = Mailings


class MailingsCreateView(CreateView):
    model = Mailings
    form_class = MailingsForm
    success_url = reverse_lazy('mailings:mailings_list')

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.owner = user
        mailing.save()
        return super().form_valid(form)


class MailingsUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailings
    form_class = MailingsForm
    success_url = reverse_lazy('mailings:mailings_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        MailingsFormset = inlineformset_factory(Mailings, Messages, MessagesForm, extra=1)

        if self.request.method == 'POST':
            context['formset'] = MailingsFormset(self.request.POST, instance=self.object)
        else:
            context['formset'] = MailingsFormset(instance=self.object)

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return MailingsForm
        if user.has_perm('mailings.can_unplug_mailings'):
            return MailingsModeratorForm
        raise PermissionDenied


class MailingsDeleteView(DeleteView):
    model = Mailings
    success_url = reverse_lazy('mailings:mailings_list')


def count_mail(request):
    """
    Возвращает общее число рассылок
    """
    context = Mailings.objects.count()
    return render(request, 'mailings/mailings_list.html', context)
