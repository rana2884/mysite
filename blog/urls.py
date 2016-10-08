from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='blog-index'),
    url(r'^blog/$', views.blog_view, name='blog-list'),
    url(r'^blog/(?P<pk>\d+)/$', views.post_view, name='blog-post'),
    url(r'^contact/$', views.contact_view, name='contact'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^captcha/', include('captcha.urls')),
]