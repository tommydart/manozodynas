from django.conf.urls import patterns, url
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import index_view, login_view
from views import WordList

urlpatterns = patterns('',
    url(r'^$', index_view, name='index'),
    url(r'^words(/(?P<page>\d+)/?)?', WordList.as_view(), name='word_list'),
    url(r'^login$', login_view, name='login'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
)
