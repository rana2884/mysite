from django.conf.urls import url, include
from django.contrib import admin
from core.decorators import login_required_message_and_redirect

#admin.autodiscover()
#admin.site.login = login_required_message_and_redirect(admin.site.login, message='Please login with staff credentials')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('blog.urls')),
    url(r'^dashboard/', include('dashboard.urls'))
]
