from django.conf.urls import url
from .views import CNVList

urlpatterns = [
    url(r'^api/v1/cvn/', CNVList.as_view(), name='user-list')
]
