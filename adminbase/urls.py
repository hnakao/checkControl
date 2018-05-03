from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url('', include(('dashboard.urls', 'dashboard'), namespace='dashboard')),
    url(r'^admin/', admin.site.urls),
]
