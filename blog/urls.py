"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve
from myblog.views import IndexView,ArichiveView,TagView,TagDetailView,BlogDetailView,AddCommentView,CategoryDetaiView,CategoryView
from myblog.feeds import BlogRssFeed
from untitled.settings import STATIC_ROOT


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', IndexView.as_view(), name='index'),
    re_path(r'^archive/$', ArichiveView.as_view(), name='archive'),
    re_path(r'^tags/$', TagView.as_view(), name='tags'),
    re_path(r'^category/$', CategoryView.as_view(), name='Category'),
    re_path(r'^tags/(?P<tag_name>\w+)$', TagDetailView.as_view(), name='tag_name'),
    re_path(r'^blog/(?P<blog_id>\d+)$', BlogDetailView.as_view(), name='blog_id'),
    re_path(r'^add_comment/$', AddCommentView.as_view(), name='add_comment'),
    re_path(r'^rss/$', BlogRssFeed(), name='rss'),
    re_path(r'^category/(?P<category_name>\w+)/$', CategoryDetaiView.as_view(), name='category_name'),
    path(r'search/', include('haystack.urls')),
    re_path(r'^static/(?P<path>.*)/$',serve, {'document_root': STATIC_ROOT}),
]
# 配置全局404页面
hander404 = 'myblog.views.page_not_found'

# 配置全局505页面
hander505 = 'myblog.views.page_errors'