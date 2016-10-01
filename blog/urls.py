from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^blog/$', views.blog),
    url(r'^blog/(?P<pk>\d+)/$', views.post),
    url(r'^contact/$', views.contact)
]