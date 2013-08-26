from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url( r'^mysite/pynotes/note/type/edit/(\d+)$', 'mysite.pynotes.views.edit_type_note' ),
    url( r'^mysite/pynotes/note/type/new/$', 'mysite.pynotes.views.add_new_note_type' ),
    url( r'^mysite/pynotes/note/type/add/$', 'mysite.pynotes.views.note_type_form' ),
    url( r'^mysite/pynotes/note/edit/(\d+)$', 'mysite.pynotes.views.note_form' ),
    url( r'^mysite/pynotes/note/delete/(\d+)$', 'mysite.pynotes.views.del_note' ),
    url( r'^mysite/pynotes/note/add/$', 'mysite.pynotes.views.note_form' ),
    url( r'^mysite/pynotes/note/new/$', 'mysite.pynotes.views.add_new_note' ),
    url( r'^mysite/pynotes/note/new/(\d+)/$', 'mysite.pynotes.views.add_new_note' ),
    url( r'^mysite/pynotes/note/(\d+)/$', 'mysite.pynotes.views.note_detail'),                   
    url( r'^mysite/pynotes/login/$', 'mysite.pynotes.views.pynotes_login' ),
    url( r'^mysite/pynotes/logout/$', 'mysite.pynotes.views.pynotes_logout' ),
    url( r'^mysite/pynotes/welcome/$', 'mysite.pynotes.views.welcome' ),
    url( r'^mysite/pynotes/about/$', 'mysite.pynotes.views.about' ),
    url( r'^mysite/pynotes/contact/$', 'mysite.pynotes.views.contact' ),
    url( r'^mysite/pynotes/register/$', 'mysite.pynotes.views.user_registration' ),
    url( r'^mysite/pynotes/$', 'mysite.pynotes.views.note_list' ),
    
    
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
