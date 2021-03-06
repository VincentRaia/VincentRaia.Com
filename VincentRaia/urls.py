"""VincentRaia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import CategoryListView, TagListView
from blog.models import Category, Tag

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin', include(admin.site.urls)),
    url(r'^blog/$', 'blog.views.index'),
    url(r'^blog/(?P<slug>[\w\-]+)/$', 'blog.views.post'),
    url(r'^$', 'landing.views.index'),
    url(r'^search', 'blog.views.getSearchResults'),
    url(r'^categories/(?P<slug>[a-zA-Z0-9-]+)/?$', CategoryListView.as_view(
        paginate_by=5,
        model=Category,
        )),
    url(r'^tags/(?P<slug>[a-zA-Z0-9-]+)/?$', TagListView.as_view(
        paginate_by=5,
        model=Tag,
        )),
)
