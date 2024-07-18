import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserModeratorForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(
            subject="Подтверждение почты",
            message=f"Перейдите по ссылке для подстверждения вашей почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list={user.email}
        )
        return super().form_valid(form)


def email_varification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class UserListView(ListView):
    model = User


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('mailings:user_list')

    def get_form_class(self):
        user = self.request.user
        if user.has_perm('mailings.can_unplug_mailings') and user.has_perm('mailings.') :
            return UserModeratorForm
        raise PermissionDenied


