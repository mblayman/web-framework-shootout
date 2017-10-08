from django.conf.urls import url

from app import views


urlpatterns = [
    url(r'^html$',
        views.index,
        name='app_html'),
    url(r'^json$',
        views.json,
        name='app_json'),
]
