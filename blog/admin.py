from django.contrib import admin

from blog.models import MyBlog


@admin.register(MyBlog)
class MeBlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'image', 'date_create')
    #exclude = 'publication_sign'
