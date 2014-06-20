from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from apps.newsletter import views

urlpatterns = patterns('',
                       # Basic
                       url(r'^$', views.landing_page, name='landing_page'),
                       )

urlpatterns += staticfiles_urlpatterns()
