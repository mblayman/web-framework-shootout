from django.conf.urls import url

from app import views


urlpatterns = [
    url(r'^$',
        views.index,
        name='app_index')
]
