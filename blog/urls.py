from django.conf.urls import url
from . import forms
from . import views

urlpatterns = [
    url(r'post_list', views.post_list, name='post_list'),
    url(r'submit', views.submit, name='submit'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
]