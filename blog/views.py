from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import MyBlogForm
from blog.models import MyBlog


def blog(request):
    return render(request, "blog/base.html")


class MyBlogView(View):

    def get(self, request):
        blogApps = MyBlog.objects.all()
        return render(request, "blog/base.html", {"blog_list": blogApps})


class MyBlogListView(ListView):
    model = MyBlog


class MyBlogDetailView(DetailView):
    model = MyBlog


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
