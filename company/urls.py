from django.conf.urls import url, patterns
from company import views

urlpatterns = patterns('',
    url(r'^(?P<company_name_slug>[\w\-]+)/$', views.login, name='login'))
