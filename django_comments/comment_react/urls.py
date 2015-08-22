from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^post', views.post, name="post"),
    url(r'^$', views.home, name="home"),
]
