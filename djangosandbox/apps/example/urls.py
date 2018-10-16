from django.conf.urls import url

from djangosandbox.apps.example.views import detail, main

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^post/(?P<post_id>\d+)/$', detail, name='detail')
]
