from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from apps.newsletter import views

urlpatterns = patterns('',
                       # Basic
                       url(r'^$', views.landing_page, name='landing_page'),
                       url(r'^calendar/$', views.calendar_page, name='calendar_page'),
                       url(r'^archive/$', views.archive_page, name='archive_page'),
                       url(r'^team/$', views.team_page, name='team_page'),
                       url(r'^test/$', views.test_page, name='test_page'),
                       url(r'^embed/email_signup$', views.embed_email_signup, name='embed_email_signup'),
                       url(r'^newsletter/(?P<newsletter_no>\d+)/$', views.newsletter_page,
                           name="newsletter"),
                       )

urlpatterns += staticfiles_urlpatterns()
