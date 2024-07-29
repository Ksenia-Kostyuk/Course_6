from django.core.cache import cache

from blog.models import MyBlog
from config.settings import CACHE_ENABLED


def get_articles_from_cache():
    """
    Получение списка статей блога из кэша. Если кэш пуст,то получение из БД.
    """
    if not CACHE_ENABLED:
        return MyBlog.objects.all()
    else:
        key = 'categories_list'
        articles = cache.get(key)
        if articles is not None:
            return articles
        else:
            articles = MyBlog.objects.all()
            cache.set(key, articles)
            return articles
