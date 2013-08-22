from django.conf.urls import patterns, url

from contacts import views
from contacts import forms

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^addcontact/', ContactForm.as_p, name='addcontact'),
    #url(r'^addcontact/', views.AddContactView.as_view(), name='addcontact'),
    url(r'^addcontact/', views.addcontact, name='addcontact'),
    url(r'^savecontact/', views.save, name='savecontact'),
    url(r'^listcontacts/', views.ListView.as_view(), name='listcontacts'),
    url(r'^(?P<pk>\d+)/detail/', views.DetailView.as_view(), name='detail'),

    url(r'^author/$', views.AuthorIndexView.as_view(), name='author-index'),
    url(r'^author/create/$', forms.AuthorCreate.as_view(), name='author-create'),
    url(r'^author/viewall/$', views.AuthorViewAllView.as_view(), name='author-viewall'),
    url(r'^author/search/(?P<word>\w+)$', views.AuthorViewSearchResult.as_view(), name='author-search'),
    url(r'^author/(?P<pk>\d+)/detail/$', views.AuthorView.as_view(), name='author-detail'),
    url(r'^author/(?P<pk>\d+)/update/$', forms.AuthorUpdate.as_view(), name='author-update'),
    url(r'^author/(?P<pk>\d+)/delete/$', forms.AuthorDelete.as_view(), name='author-delete'),
)
