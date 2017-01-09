from django.conf.urls import url
from .views import Api

urlpatterns = [
    url(r'^api/$', Api.as_view(), name="index"),
    url(r'^api/(?P<task_id>[0-9]+)/$', Api.as_view(), name="index"),
]
