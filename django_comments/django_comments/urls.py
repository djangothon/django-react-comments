from django.conf.urls import include, url
from django.contrib import admin
from django_comments.views import home, answer_list

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^answer_list', answer_list),
]
