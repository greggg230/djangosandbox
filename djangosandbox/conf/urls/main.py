from django.conf.urls import url, include
from django.contrib import admin

admin.autodiscover()


urlpatterns = [
    url(r'^example/',
        include(
            'djangosandbox.apps.example.urls',
            namespace='example'))
]
