from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^blog/$', views.blog),
    url(r'^blog/(?P<pk>\d+)/$', views.post),
    url(r'^contact/$', views.contact),
    url(r'^account/$', views.account_view),
    url(r'^logout/$', views.logout_view),
]