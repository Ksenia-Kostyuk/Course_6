from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailings.forms import MailingsForm, MessagesForm, StyleFormMixin
from mailings.models import Messages, Mailings


class MessagesListView(ListView):
    model = Messages


class MessagesDetailView(DetailView):
    model = Messages


class MessagesCreateView(StyleFormMixin, CreateView):
    model = Messages
    form_class = MessagesForm
    success_url = reverse_lazy('mailings:messages_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MailingsFormset = inlineformset_factory(Mailings, Messages, MessagesForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = MailingsFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = MailingsFormset(instance=self.object)
            return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class MessagesUpdateView(StyleFormMixin, UpdateView):
    model = Messages
    form_class = MessagesForm
    success_url = reverse_lazy('mailings:messages_list')


class MessagesDeleteView(DeleteView):
    model = Messages
    success_url = reverse_lazy('mailings:messages_list')


class MailingsListView(ListView):
    model = Mailings


class MailingsDetailView(DetailView):
    model = Mailings


class MailingsCreateView(StyleFormMixin, CreateView):
    model = Mailings
    form_class = MailingsForm
    success_url = reverse_lazy('mailings:messages_list')


class MailingsUpdateView(StyleFormMixin, UpdateView):
    model = Mailings
    form_class = MailingsForm
    success_url = reverse_lazy('mailings:messages_list')


class MailingsDeleteView(DeleteView):
    model = Mailings
    success_url = reverse_lazy('mailings:messages_list')
