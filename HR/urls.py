from django.conf.urls import url, patterns
from HR import views

urlpatterns = patterns('',
    url(r'^create_profile/$', views.create_profile, name='create_profile'))

