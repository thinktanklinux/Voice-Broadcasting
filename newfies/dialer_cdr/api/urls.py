from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from piston.doc import documentation_view
from handlers import callrequestHandler, testcallHandler, \
answercallHandler, hangupcallHandler
#from django.views.decorators.cache import cache_page


auth = HttpBasicAuthentication(realm='Newfies Application')

callrequest_handler = Resource(callrequestHandler, authentication=auth)
testcall_handler = Resource(testcallHandler, authentication=auth)
answercall_handler = Resource(answercallHandler, authentication=auth)
hangupcall_handler = Resource(hangupcallHandler, authentication=auth)

urlpatterns = patterns('',

    url(r'^callrequest[/]$', callrequest_handler),
    url(r'^callrequest/(?P<callrequest_id>[^/]+)', callrequest_handler),

    url(r'^testcall[/]$', testcall_handler),
    url(r'^answercall[/]$', answercall_handler),
    url(r'^hangupcall[/]$', hangupcall_handler),

    # automated documentation
    url(r'^doc[/]$', documentation_view),
)