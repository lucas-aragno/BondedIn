from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BondedIn.views.home', name='home'),
    # url(r'^BondedIn/', include('BondedIn.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

   

    url(r'^test/?$', 'linkedinapp.views.test'),
    url(r'^login/?$', 'linkedinapp.views.oauth_login'),
    url(r'^logout/?$', 'linkedinapp.views.oauth_logout'),
    url(r'^login/authenticated/?$', 'linkedinapp.views.oauth_authenticated'),
    url(r'^$','linkedinapp.views.home'),
    url(r'^list/(?P<skill>\S+)/(?P<location>\S*)$','linkedinapp.views.list'),
)
