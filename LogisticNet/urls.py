from django.conf.urls import include, url
from django.contrib import admin
from company import views
from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/HR/create_profile/'

urlpatterns = [
    url(r'^$', 'LogisticNet.views.home', name='home'),
    url(r'(?P<company_name_slug>^adam)/$', views.login, name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^HR/',include('HR.urls')),
    url(r'^mission/',include('mission.urls')),
]
