from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateView, email_varification, UserListView, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('edit/<int:pk>/', UserUpdateView.get_form_class, name='user_blok'),
    path('email-confirm/<str:token>/', email_varification, name='email-confirm'),

]
