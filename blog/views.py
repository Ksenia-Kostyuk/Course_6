from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import MyBlogForm
from blog.models import MyBlog
from blog.services import get_articles_from_cache


class MyBlogView(View):

    def get(self, request):
        blogApps = MyBlog.objects.all()
        return render(request, "blog/base.html", {"blog_list": blogApps})


class MyBlogListView(ListView):
    template_name = 'blog/blog_list.html'
    model = MyBlog

    def get_queryset(self, *args, **kwargs):
        queryset = get_articles_from_cache().filter(publication_sign=True)
        return queryset


class MyBlogDetailView(DetailView):
    model = MyBlog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class MyBlogCreateView(CreateView):
    model = MyBlog
    form_class = MyBlogForm
    success_url = reverse_lazy('mailings:blog_list')

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.owner = user
        message.save()
        return super().form_valid(form)


class MyBlogUpdateView(UpdateView):
    model = MyBlog
    form_class = MyBlogForm
    success_url = reverse_lazy('mailings:blog_list')


class MyBlogDeleteView(DeleteView):
    model = MyBlog
    success_url = reverse_lazy('mailings:blog_list')
