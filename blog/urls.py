from django.urls import path

from blog.apps import BlogConfig
from blog.views import blog, MyBlogListView

app_name = BlogConfig.name

urlpatterns = [
    path('', blog, name='base_blog'),
    path('', MyBlogListView.as_view(), name='blog_list')
]