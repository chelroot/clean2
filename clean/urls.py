from django.conf.urls import patterns, include, url
from django.contrib import admin
from mainapp.views import index, about, post, foto, contact
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'clean.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index, name='index'),
    url(r'^about/$', about, name='about'),
    url(r'^post/$', post, name='post'),
    url(r'^foto/$', foto, name='foto'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^admin/', include(admin.site.urls)),


    # url(r'^clean/$', index, name='index'),
    # url(r'^clean/about/$', about, name='about'),
    # url(r'^clean/post/$', post, name='post'),
    # url(r'^clean/contact/$', contact, name='contact'),
    # url(r'^clean/admin/', include(admin.site.urls)),
    #

)


