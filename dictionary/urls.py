from django.conf.urls import url
from dictionary.views import *

urlpatterns = [
    url(r'dict/$', big_dictionary, name='big_dict'),
    url(r'dict/(?P<first_letter>[a-z])', page_letter, name='big_dict')
]
