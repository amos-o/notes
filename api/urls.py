from django.conf.urls import url, include

from api.views import RegisterView

urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'', name='notes')
    # url(r'', name='detail')
]
