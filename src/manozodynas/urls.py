from django.conf.urls import patterns, url
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import index_view, login_view, vote_view
from views import vote_delete_view, word_delete_view
from views import WordList
from views import CreateWord, WordView

urlpatterns = patterns('',
    url(r'^$', index_view, name='index'),
    url(r'^words(/(?P<page>\d+)/?)?', WordList.as_view(), name='word_list'),
    url(r'^new_word$', CreateWord.as_view(), name='new_word'),
    url(r'^word/(?P<id>\d+)$', WordView.as_view(), name='word_view'),
    url(r'^translation/(?P<id>\d+)/vote$', vote_view, name='vote'),
    url(r'^translation/(?P<id>\d+)/delete$', vote_delete_view, name='translation_delete'),
    url(r'^word/(?P<id>\d+)/delete$', word_delete_view, name='word_delete'),
    url(r'^login$', login_view, name='login'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
)
