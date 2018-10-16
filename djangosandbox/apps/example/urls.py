from django.conf.urls import url

from djangosandbox.apps.example.views import DetailView, IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='main'),
    url(r'^post/(?P<post_id>\d+)/$', DetailView.as_view(), name='detail')
]
