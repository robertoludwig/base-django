
from django.conf.urls import url
from django.contrib import admin

from webapp.core.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
]