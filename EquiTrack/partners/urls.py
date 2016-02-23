from __future__ import absolute_import

__author__ = 'jcranwellward'

from django.conf.urls import patterns, url, include

from .views import (
    LocationView,
    PortalDashView,
    PortalLoginFailedView,
    PartnerStaffMemberPropertiesView,
    PartnerInterventionsView,
    PcaPDFView,
)


urlpatterns = patterns(
    '',
    url(r'^$', PortalDashView.as_view()),
    url(r'^accounts/loginfailed/(?P<email>.+)/$', PortalLoginFailedView.as_view(), name='sociallogin_notamember'),
    url(r'^locations/$', LocationView.as_view(), name='locations'),
    url(r'^agreement/(?P<agr>\d+)/pdf', PcaPDFView.as_view()),

    url(r'^staffmember/(?P<pk>\d+)/$', PartnerStaffMemberPropertiesView.as_view()),
    url(r'^api/interventions/$', PartnerInterventionsView.as_view()),

    # auth and registration for partners
    #url(r'', include('registration.auth_urls')),
)
