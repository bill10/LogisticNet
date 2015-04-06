from django.conf.urls import url, patterns
from mission import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='mission_index'))
