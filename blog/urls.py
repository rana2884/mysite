from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^blog/$', views.blog_view),
    url(r'^blog/(?P<pk>\d+)/$', views.post_view),
    url(r'^contact/$', views.contact_view),
    url(r'^logout/$', views.logout_view),
    url(r'^captcha/', include('captcha.urls')),
]