from django.conf.urls import url, include
from article import views

urlpatterns = [
    url(r'^1/', views.basic_one, name='basic_one'),
    url(r'^2/', views.basic_two),
    url(r'^3/', views.basic_three_simple),
    url(r'^articles/all/$', views.articles),
    url(r'^articles/get/(?P<article_id>\d+)/$', views.article, name='get'),
    url(r'^articles/addlike/(?P<article_id>\d+)/$', views.addlike, name='addlike'),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', views.addcomment, name='addcomment'),
    url(r'^page/(\d+)/$', views.articles, name='page'),
    url(r'^$', views.articles, name='main'),
]
