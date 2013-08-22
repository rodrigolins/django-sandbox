from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tutorial01.views.home', name='home'),
    # url(r'^tutorial01/', include('tutorial01.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^contacts/', include('contacts.urls', namespace="contacts")),
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^$', 'index.html')
)
