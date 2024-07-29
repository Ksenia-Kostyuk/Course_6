from django.urls import path

from blog.apps import BlogConfig
from blog.views import MyBlogListView

app_name = BlogConfig.name

urlpatterns = [
    path('', MyBlogListView.as_view(), name='blog_list'),
]