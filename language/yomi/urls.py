from django.conf.urls import url
from yomi import views

urlpatterns = [
   url(r'^yomi/$', views.yomi, name='yomi'),
]


